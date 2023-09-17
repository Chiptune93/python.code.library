import multiprocessing
import threading

# 작업 함수 정의
def do_work(val):
    for i in range(val):
        print(f"작업 {i + 1}")

if __name__ == "__main__":
    # 프로세스 생성
    process1 = multiprocessing.Process(target=do_work, args=(5,))
    process2 = multiprocessing.Process(target=do_work, args=(5,))

    # 스레드 생성
    thread1 = threading.Thread(target=do_work, args=(5,))
    thread2 = threading.Thread(target=do_work, args=(5,))

    # 프로세스 시작
    process1.start()
    process2.start()

    # 스레드 시작
    thread1.start()
    thread2.start()

    # 프로세스와 스레드가 종료될 때까지 대기
    process1.join()
    process2.join()
    thread1.join()
    thread2.join()

    print("모든 작업이 완료되었습니다.")
