#-*-coding: utf-8 -*-

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
                 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def read_textfile():
    with open('textFile.txt', encoding='utf-16') as t:
        contents = t.read()
        print(contents)


def korean_to_be_englished(korean_word):
    r_lst = []
    for w in list(korean_word.strip()):

        if '가' <= w <= '힣':
            ## 588개 마다 초성이 바뀜.
            ch1 = (ord(w) - ord('가')) // 588
            ## 중성은 총 28가지 종류
            ch2 = ((ord(w) - ord('가')) - (588 * ch1)) // 28
            ch3 = (ord(w) - ord('가')) - (588 * ch1) - 28 * ch2
            r_lst.append([CHOSUNG_LIST[ch1], JUNGSUNG_LIST[ch2], JONGSUNG_LIST[ch3]])

        else: ## 영어인 경우 구분해서 작성함.
            r_lst.append([w])
    return r_lst

def korean_encrypt(r_lst):
    new_lst =[]

    for i in enumerate(r_lst):
        if i is 'ㄱ':
            new_lst.append('Z')
        else:
            new_lst.append('LOL')

print(korean_to_be_englished("이승훈a"))

def korean_word_to_initials(korean_word):
    """
    한글을 입력받아서 한글 초성에 따라서 이니셜로 변환해줍니다.
    한국 성의 경우 조금 다르게 변환되는데 '박' ==> 'Park'인 부분은 반영하지 않음
    """
    w_to_k = {'ㄱ':'K', 'ㄲ':'G', 'ㄴ':'N', 'ㄷ':'D', 'ㄸ':'D', 'ㄹ':'R', 'ㅁ':'M', 'ㅂ':'B',
              'ㅃ':'B', 'ㅅ':'S', 'ㅈ':'J', 'ㅉ':'J', 'ㅊ':'C', 'ㅌ':'T', 'ㅍ':'P', 'ㅎ':'H'}
    r_lst = []
    for i, w in enumerate(korean_to_be_englished(korean_word)):
        if w[0] in w_to_k.keys():
            r_lst.append( w_to_k[w[0]] )
        else:
            if w[1] in ['ㅑ', 'ㅕ', 'ㅛ', 'ㅠ', 'ㅖ']:
                r_lst.append('Y')
            elif w[1] in ['ㅝ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅜ', 'ㅞ', 'ㅟ']:
                r_lst.append('W')
            elif w[1] in ['ㅔ', 'ㅡ', 'ㅢ']:
                r_lst.append('E')
            elif w[1] in ['ㅏ', 'ㅐ']:
                r_lst.append('A')
            elif w[1] in ['ㅓ']:
                r_lst.append('U')
            elif w[1] in ['ㅗ']:
                r_lst.append('O')
            elif w[1] in ['ㅣ']:
                if i==0:
                    r_lst.append('L')
                else:
                    r_lst.append('I')
            else:
                return 'not applicable'
    return "".join(r_lst)

#def korean_encrypt(korean_word):

### test case
'''
test_cases = ['이승훈', '전지현', '하정우', '정우성', '박상원', '정유미', '김연우', '윤종신']
for case in test_cases:
    print("{} ==> {}".format(case, korean_word_to_initials(case)))

'''

'''
reference
https://frhyme.github.io/python/python_korean_englished/
https://github.com/neotune/python-korean-handler/blob/master/korean_handler.py
http://blog.daum.net/_blog/BlogTypeView.do?blogid=06WNj&articleno=15981300&categoryId=326462&regdt=20180112094830
'''