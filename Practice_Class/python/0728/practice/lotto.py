# 여기에 필요한 모듈을 추가합니다.
import random
import datetime
import json

class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
<<<<<<< HEAD
        self.number_lines = []

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        pass
        for i in range(n):
            random_lotto = sorted(random.sample(range(1, 46), 6))
            self.number_lines.append(random_lotto)

    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        year, month, day = map(int, Lotto.get_draw_date(draw_number))
        date = datetime.date(year, month, day).weekday()
        week = {"월" : 0, "화" : 1, "수" : 2, "목" : 3, "금" : 4, "토" : 5, "일" : 6}
        when = list(week.keys())[date]
        
        print('======================================')
        print(f'           제 {draw_number} 회 로또       ')
        print('======================================')
        print(f'추첨일 : {year}/{month}/{day} ({when})')
        print('======================================')
        for idx, lotto_num in enumerate(self.number_lines, start = 65):
            print(f'{chr(idx)} : {lotto_num}')
=======
        self.number_lines = list()

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        for i in range(n):
            lotto_num = sorted(random.sample(list(range(1, 46)), 6))
            self.number_lines.append(lotto_num)

    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        year, month, day = map(int,Lotto.get_draw_date(draw_number))
        today = datetime.datetime(year, month, day)
        when = {0 : '월', 1 : '화', 2 : '수', 3 : '목', 4 : '금', 5 : '토', 6 : '일'}
        line = '==================================='
        print(line)
        print(f'          {f"제 {draw_number} 회 로또"}')
        print(line)
        print(f'추첨일 : {today.year}/{today.month}/{today.day} ({when[today.weekday()]})')
        print(line)
        for i in range(len(self.number_lines)):
            print(f'{chr(i + 65)} : {self.number_lines[i]}')
>>>>>>> 3122dfea671cc94038505f5ec7ef9814bfce4374

    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        main_numbers, bonus_number = Lotto.get_lotto_numbers(draw_number)
<<<<<<< HEAD

        print('======================================')
        print(f'당첨 번호 : {main_numbers} + {bonus_number}')  
        print('======================================')
        for line_num in range(len(self.number_lines)):
            line = self.number_lines[line_num]
            same_main_counts, is_bonus = Lotto.get_same_info(main_numbers, bonus_number, line)
            ranking = Lotto.get_ranking(same_main_counts, is_bonus)
            if is_bonus == True and ranking == 2:
                print(f'{chr(65 + line_num)} : {same_main_counts}개 일치 + 보너스 일치 ({ranking}등 당첨!)')
            elif is_bonus == True and 3 <= ranking <= 5:
                print(f'{chr(65 + line_num)} : {same_main_counts}개 일치 + 보너스 일치 ({ranking}등 당첨!)')
            elif is_bonus == True and ranking == -1:
                print(f'{chr(65 + line_num)} : {same_main_counts}개 일치 + 보너스 일치 (낙첨)')
            elif ranking == 1 or 3 <= ranking <=5:
                print(f'{chr(65 + line_num)} : {same_main_counts}개 일치 ({ranking}등 당첨!)')
            else:
                print(f'{chr(65 + line_num)} : {same_main_counts}개 일치 (낙첨)')
                
=======
        line = '==================================='
        print(line)
        print(f'당첨 번호 : {main_numbers} + {bonus_number}')
        print(line)
        for i in range(len(self.number_lines)):
            same_main_counts, is_bonus = Lotto.get_same_info(main_numbers, bonus_number, self.number_lines[i])
            ranking = Lotto.get_ranking(same_main_counts, is_bonus)
            if is_bonus == True and (ranking != 1 or ranking != 2):
                print(f'{chr(i + 65)} : {same_main_counts}개 + 보너스 일치 (낙첨)')
            elif ranking != -1:
                print(f'{chr(i + 65)} : {same_main_counts}개 일치 ({ranking}등 당첨!)')
            else:
                print(f'{chr(i + 65)} : {same_main_counts}개 일치 (낙첨)')
>>>>>>> 3122dfea671cc94038505f5ec7ef9814bfce4374

    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
<<<<<<< HEAD
        draw_date_open = open(f'data/lotto_{draw_number}.json', encoding = 'utf-8')
        draw_data_json = json.load(draw_date_open)
        year, month, day = draw_data_json['drwNoDate'].split('-')
=======
        number_file = open(f'data/lotto_{draw_number}.json', encoding = 'utf-8')
        draw_number_date = json.load(number_file)['drwNoDate']
        year, month, day = draw_number_date.split('-')
>>>>>>> 3122dfea671cc94038505f5ec7ef9814bfce4374
        return year, month, day

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
<<<<<<< HEAD
        draw_num_open = open(f'data/lotto_{draw_number}.json', encoding = 'utf-8')
        draw_num_data = json.load(draw_num_open)
        main_numbers = []
        bonus_number = draw_num_data['bnusNo']
        for k, v in draw_num_data.items():
            if k.startswith('drwtNo'):
                main_numbers.append(int(v))
        main_numbers.sort()
=======
        lotto_file = open(f'data/lotto_{draw_number}.json', encoding = 'utf-8')
        lotto_data = json.load(lotto_file)
        main_numbers = sorted([lotto_data.get(f'drwtNo{i}') for i in range(1, 7)])
        #main_numbers = sorted([i for i in lotto_date[startswith]])
        bonus_number = lotto_data.get('bnusNo')
>>>>>>> 3122dfea671cc94038505f5ec7ef9814bfce4374
        return main_numbers, bonus_number

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        same_main_counts = 0
        is_bonus = False
<<<<<<< HEAD
        for each_num in line:
            if each_num in main_numbers:
                same_main_counts += 1
            elif each_num == bonus_number:
                is_bonus = True
=======
        for i in main_numbers:
            same_main_counts += line.count(i)
        if bonus_number in line:
            is_bonus = True
        else:
            is_bonus = False
>>>>>>> 3122dfea671cc94038505f5ec7ef9814bfce4374
        return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
<<<<<<< HEAD
        ranking = 0
=======
        ranking = ''
>>>>>>> 3122dfea671cc94038505f5ec7ef9814bfce4374
        if same_main_counts == 6:
            ranking = 1
        elif same_main_counts == 5 and is_bonus == True:
            ranking = 2
        elif same_main_counts == 5:
            ranking = 3
        elif same_main_counts == 4:
            ranking = 4
        elif same_main_counts == 3:
            ranking = 5
        else:
            ranking = -1
        return ranking