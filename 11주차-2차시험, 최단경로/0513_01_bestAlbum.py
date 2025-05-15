"""
    프로그래머스 - 베스트 앨범
"""

def solution(genres, plays):
    from collections import defaultdict

    genre_total = defaultdict(int)        # 장르별 총 재생 횟수
    genre_dict = defaultdict(list)        # 장르별 곡 정보 저장

    # 1단계: 정보 정리
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        genre_total[genre] += play
        genre_dict[genre].append((idx, play))

    # 2단계: 장르 정렬 (총 재생 수 내림차순)
    sorted_genres = sorted(genre_total.keys(), key=lambda g: genre_total[g], reverse=True)

    answer = []
    for genre in sorted_genres:
        # 3단계: 장르별 노래 정렬 (재생 수 내림차순, 고유 번호 오름차순)
        sorted_songs = sorted(genre_dict[genre], key=lambda x: (-x[1], x[0]))
        
        # 4단계: 최대 2곡 추가
        for song in sorted_songs[:2]:
            answer.append(song[0])
    return answer

# [4, 1, 3, 0]
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))