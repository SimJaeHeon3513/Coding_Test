def solution(message, spoiler_ranges):
    # 1. 메시지 내 모든 단어의 [시작, 끝, 단어] 정보 추출
    import re
    words_info = []
    for m in re.finditer(r'\S+', message): # 공백이 아닌 연속된 문자열(단어) 찾기
        words_info.append({
            'start': m.start(),
            'end': m.end() - 1,
            'text': m.group()
        })

    # 2. 노출된 단어(스포 구간 밖)와 스포일러 단어 구분하기
    # 모든 인덱스에 대해 스포 구간인지 아닌지 마킹해두면 편합니다.
    is_spoiler_idx = [False] * len(message)
    for s, e in spoiler_ranges:
        for i in range(s, e + 1):
            is_spoiler_idx[i] = True

    exposed_words = set()   # 스포 구간이 아닌 곳에 등장한 단어들
    spoiler_word_indices = [] # 스포 방지 단어들의 인덱스 번호(words_info 기준)

    for i, info in enumerate(words_info):
        is_spoiler_word = False
        # 단어의 인덱스 중 하나라도 스포 구간에 포함되는지 확인
        for idx in range(info['start'], info['end'] + 1):
            if is_spoiler_idx[idx]:
                is_spoiler_word = True
                break
        
        if is_spoiler_word:
            spoiler_word_indices.append(i)
        else:
            exposed_words.add(info['text'])

    # 3. 중요한 단어 카운트하기
    important_count = 0
    already_counted = set() # 이전에 공개된 중요한 단어 중복 방지

    for idx in spoiler_word_indices:
        word_text = words_info[idx]['text']
        
        # 조건: 노출된 적 없고 + 이전에 카운트된 적 없음
        if word_text not in exposed_words and word_text not in already_counted:
            important_count += 1
            already_counted.add(word_text)

    return important_count