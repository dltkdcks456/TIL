## Mockito란?

· Mock 객체를 쉽게 만들고, 관리하고, 검증할 수 있는 방법을 제공하는 프레임워크

- Mock: 진짜 객체와 비슷하게 동작하지만, 프로그래머가 직접 행동을 관리하는 객체
- 공홈 https://site.mockito.org/

· 테스트를 작성하는 자바 개발자의 45%가 사용하는 Mock 프레임워크

- 2021년 젯브레인 설문조사 기준 https://www.jetbrains.com/lp/devecosystem-2021/java/

· 대체제: EasyMock, JMock

· 애플리케이션에서 데이터베이스, 외부 API 등을 테스트할 때, 해당 제품들이 어떻게 작동하는지 항상 사용하면서 테스트를 작성한다면 매우 불편할 것이다. 이럴 때 어떻게 작동하는지 예측을 하여 Mock 객체를 만들어서 사용하면, 편리한 테스트가 가능하다.

- ex) dao 또는 repository가 어떻게 작동하는지 Mockito를 이용해 만들어 놓으면,

dao, repository 객체를 구현하기 전에도 테스트를 작성할 수 있다.

### Mockito 설정

```java
// application.yml

// mockito
dependencies{
    testImplementation 'org.mockito:mockito-core:3.11.2'
    testImplementation 'org.mockito:mockito-junit-jupiter:3.11.2'
    testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine:5.7.0'
}
```

### Mockito 예제

- 테스트를 위해 실제 객체와 비슷한 객체를 만드는 것을 모킹(Mocking)이라고 한다.
- 테스트하려는 객체가 복잡한 의존성을 가진 경우, 모킹한 객체를 이용하면 의존성을 단절시킬 수 있다.



```java
@AutoConfigureMockMvc
@SpringBootTest
@EnableMockMvc
class PlaceApiControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ObjectMapper objectMapper;

    @MockBean
    private PlaceService placeService;

    @Test
    @DisplayName("시/도 정보 가져오기")
    @WithMockUser(username = "테스트_최고관리자", roles = {"SUPER"})
    // HTTP Status 200, Service에서 Sido 데이터를 형식에 맞게 잘 가져오는지 확인
    public void SidoControllerTest() throws Exception {
        //given
        // sido에 관한 Mock 데이터 생성
        List<Sido> sidoResponseDto = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            sidoResponseDto.add(new Sido("code", "test"));
        }
        // listSido를 실행할 때 sidoMockList를 불러온다.
        when(placeService.listSido()).thenReturn(sidoResponseDto);

        //when
        // get으로 sido를 불러오는 요청을 보낸다.
        ResultActions resultActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/sido"));

        //then
        //OK를 호출하는지 확인
        MvcResult mvcResult = resultActions.andExpect(status().isOk()).andReturn();

        // 받은 데이터를 sido List로 변환
        Sido[] sido = new Gson().fromJson(mvcResult.getResponse().getContentAsString(), Sido[].class);
        List<Sido> sidoList = Arrays.asList(sido);

        // 해당 리스트의 개수가 5개인지 확인
        assertThat(sidoList.size()).isEqualTo(5);
        assertThat(sidoList.get(0).getSidoCode()).isEqualTo("code");
    }

    @Test
    @DisplayName("구/군 정보 가져오기")
    @WithMockUser(username = "테스트_최고관리자", roles = {"SUPER"})
    // HTTP Status 200, Service에서 gugun 데이터를 형식에 맞게 잘 가져오는지 확인
    public void gugunControllerTest() throws Exception {
        //given
        // Sido Mock 데이터
        List<Sido> sidoList = new ArrayList<>();
        sidoList.add(new Sido("1", "Seoul"));

        // gugun Mock 데이터
        List<GugunDto> gugunDtoList = new ArrayList<>();
        gugunDtoList.add(new GugunDto("1", "GangNam"));
        gugunDtoList.add(new GugunDto("2", "GangBuk"));

        // stub
        when(placeService.listGugun(1)).thenReturn(gugunDtoList);

        //when
        ResultActions resultActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/gugun/1"));

        //then
        MvcResult mvcResult = resultActions.andExpect(status().isOk()).andReturn();

        GugunDto[] gugunDto = new Gson().fromJson(mvcResult.getResponse().getContentAsString(), GugunDto[].class);
        List<GugunDto> gugunDtoListData = Arrays.asList(gugunDto);

        assertThat(gugunDtoListData.size()).isEqualTo(2);
        assertThat(gugunDtoListData.get(0).getGugunCode()).isEqualTo("1");
    }

    @Test
    @DisplayName("장소 상세 정보 가져오기")
    @WithMockUser(username = "테스트_최고관리자", roles = {"SUPER"})
    // 내용이 있을 경우, Http Status 200, 해당 ResponseDto 반환 확인
    // 내용이 없을 경우, Http Status 204, null 반환 확인
    public void detailPlaceControllerTest() throws Exception {
        //given
        TourResponseDto tourResponseDto = TourResponseDto.builder().type("tour").build();
        FestivalResponseDto festivalResponseDto = FestivalResponseDto.builder().type("festival").startDate("20230326").build();
        AccommodationResponseDto accommodationResponseDto = AccommodationResponseDto.builder().type("accommodation").build();
        RestaurantResponseDto restaurantResponseDto = RestaurantResponseDto.builder().type("restaurant").build();
        CafeResponseDto cafeResponseDto = CafeResponseDto.builder().type("cafe").build();
        ShoppingResponseDto shoppingResponseDto = ShoppingResponseDto.builder().type("shopping").build();
        LeisureResponseDto leisureResponseDto = LeisureResponseDto.builder().type("leisure").build();
        CultureResponseDto cultureResponseDto = CultureResponseDto.builder().type("culture").build();

        //stub
        when(placeService.detailTour(anyLong(), anyLong())).thenReturn(tourResponseDto)
                .thenReturn(null);
        when(placeService.detailFestival(anyLong(), anyLong())).thenReturn(festivalResponseDto)
                .thenReturn(null);
        when(placeService.detailAccommodation(anyLong(), anyLong())).thenReturn(accommodationResponseDto)
                .thenReturn(null);
        when(placeService.detailRestaurant(anyLong(), anyLong())).thenReturn(restaurantResponseDto)
                .thenReturn(null);
        when(placeService.detailCafe(anyLong(), anyLong())).thenReturn(cafeResponseDto)
                .thenReturn(null);
        when(placeService.detailShopping(anyLong(), anyLong())).thenReturn(shoppingResponseDto)
                .thenReturn(null);
        when(placeService.detailLeisure(anyLong(), anyLong())).thenReturn(leisureResponseDto)
                .thenReturn(null);
        when(placeService.detailCulture(anyLong(), anyLong())).thenReturn(cultureResponseDto)
                .thenReturn(null);

        //1. when(내용이 모두 존재할 경우)
        ResultActions resultTourActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/places/detail/users/1/placeId/1/type/tour"));
        ResultActions resultFestivalActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/places/detail/users/1/placeId/1/type/festival"));
        ResultActions resultAccommodationActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/places/detail/users/1/placeId/1/type/accommodation"));
        ResultActions resultRestaurantActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/places/detail/users/1/placeId/1/type/restaurant"));
        ResultActions resultCafeActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/places/detail/users/1/placeId/1/type/cafe"));
        ResultActions resultShoppingActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/places/detail/users/1/placeId/1/type/shopping"));
        ResultActions resultLeisureActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/places/detail/users/1/placeId/1/type/leisure"));
        ResultActions resultCultureActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/places/detail/users/1/placeId/1/type/culture"));

        //1. then
        // tour verify
        MvcResult tourMvcResult = resultTourActions.andExpect(status().isOk()).andReturn();
        TourResponseDto tourResponse = new Gson().fromJson(tourMvcResult.getResponse().getContentAsString(), tourResponseDto.getClass());
        assertThat(tourResponse.getType()).isEqualTo("tour");

        // festival verify
        MvcResult festivalMvcResult = resultFestivalActions.andExpect(status().isOk()).andReturn();
        FestivalResponseDto festivalResponse = new Gson().fromJson(festivalMvcResult.getResponse().getContentAsString(), festivalResponseDto.getClass());
        assertThat(festivalResponse.getType()).isEqualTo("festival");

        //accommodation verify
        MvcResult accommodationMvcResult = resultAccommodationActions.andExpect(status().isOk()).andReturn();
        AccommodationResponseDto accommodationResponse = new Gson().fromJson(accommodationMvcResult.getResponse().getContentAsString(), accommodationResponseDto.getClass());
        assertThat(accommodationResponse.getType()).isEqualTo("accommodation");

        //restaurant verify
        MvcResult restaurantMvcResult = resultRestaurantActions.andExpect(status().isOk()).andReturn();
        RestaurantResponseDto restaurantResponse = new Gson().fromJson(restaurantMvcResult.getResponse().getContentAsString(), restaurantResponseDto.getClass());
        assertThat(restaurantResponse.getType()).isEqualTo("restaurant");

        //cafe verify
        MvcResult cafeMvcResult = resultCafeActions.andExpect(status().isOk()).andReturn();
        CafeResponseDto cafeResponse = new Gson().fromJson(cafeMvcResult.getResponse().getContentAsString(), cafeResponseDto.getClass());
        assertThat(cafeResponse.getType()).isEqualTo("cafe");

        //shopping verify
        MvcResult shoppingMvcResult = resultShoppingActions.andExpect(status().isOk()).andReturn();
        ShoppingResponseDto shoppingResponse = new Gson().fromJson(shoppingMvcResult.getResponse().getContentAsString(), shoppingResponseDto.getClass());
        assertThat(shoppingResponse.getType()).isEqualTo("shopping");

        //leisure verify
        MvcResult leisureMvcResult = resultLeisureActions.andExpect(status().isOk()).andReturn();
        LeisureResponseDto leisureResponse = new Gson().fromJson(leisureMvcResult.getResponse().getContentAsString(), leisureResponseDto.getClass());
        assertThat(leisureResponse.getType()).isEqualTo("leisure");

        //culture verify
        MvcResult cultureMvcResult = resultCultureActions.andExpect(status().isOk()).andReturn();
        CultureResponseDto cultureResponse = new Gson().fromJson(cultureMvcResult.getResponse().getContentAsString(), cultureResponseDto.getClass());
        assertThat(cultureResponse.getType()).isEqualTo("culture");

        //2. when(내용이 존재하지 않을 경우)
        ResultActions resultEmptyTourActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/places/detail/users/1/placeId/1/type/tour"));
        ResultActions resultEmptyFestivalActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/places/detail/users/1/placeId/1/type/festival"));
        ResultActions resultEmptyAccommodationActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/places/detail/users/1/placeId/1/type/accommodation"));
        ResultActions resultEmptyRestaurantActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/places/detail/users/1/placeId/1/type/restaurant"));
        ResultActions resultEmptyCafeActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/places/detail/users/1/placeId/1/type/cafe"));
        ResultActions resultEmptyShoppingActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/places/detail/users/1/placeId/1/type/shopping"));
        ResultActions resultEmptyLeisureActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/places/detail/users/1/placeId/1/type/leisure"));
        ResultActions resultEmptyCultureActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/places/detail/users/1/placeId/1/type/culture"));

        //then(null값 반환 및 204 상태 응답)
        // tour verify
        MvcResult tourEmptyMvcResult = resultEmptyTourActions.andExpect(status().isNoContent()).andReturn();
        assertThat(tourEmptyMvcResult.getResponse().getContentAsString()).isEmpty();

        // festival verify
        MvcResult festivalEmptyMvcResult = resultEmptyFestivalActions.andExpect(status().isNoContent()).andReturn();
        assertThat(festivalEmptyMvcResult.getResponse().getContentAsString()).isEmpty();

        // accommodation verify
        MvcResult accommodationEmptyMvcResult = resultEmptyAccommodationActions.andExpect(status().isNoContent()).andReturn();
        assertThat(accommodationEmptyMvcResult.getResponse().getContentAsString()).isEmpty();

        // restaurant verify
        MvcResult restaurantEmptyMvcResult = resultEmptyRestaurantActions.andExpect(status().isNoContent()).andReturn();
        assertThat(restaurantEmptyMvcResult.getResponse().getContentAsString()).isEmpty();

        // cafe verify
        MvcResult cafeEmptyMvcResult = resultEmptyCafeActions.andExpect(status().isNoContent()).andReturn();
        assertThat(cafeEmptyMvcResult.getResponse().getContentAsString()).isEmpty();

        // shopping verify
        MvcResult shoppingEmptyMvcResult = resultEmptyShoppingActions.andExpect(status().isNoContent()).andReturn();
        assertThat(shoppingEmptyMvcResult.getResponse().getContentAsString()).isEmpty();

        // leisure verify
        MvcResult leisureEmptyMvcResult = resultEmptyLeisureActions.andExpect(status().isNoContent()).andReturn();
        assertThat(leisureEmptyMvcResult.getResponse().getContentAsString()).isEmpty();

        // culture verify
        MvcResult cultureEmptyMvcResult = resultEmptyCultureActions.andExpect(status().isNoContent()).andReturn();
        assertThat(cultureEmptyMvcResult.getResponse().getContentAsString()).isEmpty();

        // get 요청 시 type이 위 영역에 속하지 않을 시 404에러 발생
        ResultActions resultEmptyPlaceActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/places/detail/users/1/placeId/1/type/32"));
        resultEmptyPlaceActions.andExpect(status().isBadRequest());
    }

    @Test
    @DisplayName("검색어 자동완성")
    @WithMockUser(username = "테스트_최고관리자", roles = {"SUPER"})
    // 검색어가 있을 경우, Http Status 200, 해당 ResponseDto 반환 확인
    // 검색어가 없을 경우, Http Status 204, null 반환 확인
    public void searchControllerTest() throws Exception {
        //given
        List<AutoCompleteResponseDto> list = new ArrayList<>();
        list.add(AutoCompleteResponseDto.builder().placeId(1L).name("name1").address("address1").thumbNailUrl("url1").type("type1").build());
        list.add(AutoCompleteResponseDto.builder().placeId(2L).name("name2").address("address2").thumbNailUrl("url2").type("type2").build());

        when(placeService.autoCompleteSearchPlacesByName(anyString())).thenReturn(list);

        //when(검색어가 존재할 경우)
        ResultActions resultActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/places/auto/test"));

        //then
        MvcResult mvcResult = resultActions.andExpect(status().isOk()).andReturn();
        AutoCompleteResponseDto[] responseDto = new Gson().fromJson(mvcResult.getResponse().getContentAsString(), AutoCompleteResponseDto[].class);
        List<AutoCompleteResponseDto> resultData = Arrays.asList(responseDto);
        assertThat(resultData.size()).isEqualTo(2);

        // when(검색어가 없을 경우)
        ResultActions resultEmptyActions = mockMvc.perform(MockMvcRequestBuilders.get("/api/places/auto/"));

        // then
        MvcResult mvcEmptyResult = resultEmptyActions.andExpect(status().isNoContent()).andReturn();
        assertThat(mvcEmptyResult.getResponse().getContentAsString()).isEmpty();
    }
}
```