1. Auto Scaling이 필요한 이유와 역할 설명해보기

   - 정확한 수의 EC2 인스턴스를 보유하도록 보장

     - 그룹의 최소 인스턴스 숫자와 최대 인스턴스 숫자를 관리
     - 만약 애플리케이션을 실행하기 위해 인스턴스가 3개가 필요하다면, 3대 이상의 인스턴스가 항상 떠있을 수 있게 보장한다.
     - 최소 숫자 이하로 내려가지 않도록 인스턴스 숫자를 유지 (인스턴스 추가)
     - 최대 숫자 이상 늘어자니 않도록 인스턴스 숫자 유지 (인스턴스 삭제)

   - 다양한 스케일링 정책 적용 가능
     - CPU의 부하에 따라 인스턴스 크기 늘리기/줄이기 (오후 2시가 되면 게임 접속 트래픽이 많으니 인스턴스 확 올리고, 새벽 2시가 되면 접속 트래픽이 낮으니 인스턴스를 내린다.)
   - 가용영역에 인스턴스가 골고루 분산될 수 있도록 인스턴스를 분배
     - 서비스 장애가 발생하더라도 문제없이 서비스 이용

2. EC2 인스턴스 생성하기(서울 리전, Bitnami WordPress, t2.micro)
![1](https://github.com/sub-blind/oz_front/assets/58137602/59716f58-4860-462d-809b-7d5f771441e0)
3. ALB 생성하기
![3](https://github.com/sub-blind/oz_front/assets/58137602/6d518965-91b6-4c4c-bf52-86a29bf510c2)
4. 생선한 EC@ 인스턴스를 기반으로 AMI 생성하기
![4](https://github.com/sub-blind/oz_front/assets/58137602/c12be4c1-0352-45a1-89a2-474c7152177b)
5. auto Scaling Group 만들기
![5](https://github.com/sub-blind/oz_front/assets/58137602/af1a359c-9fff-4860-8cfa-215fa260dee7)
6. EC@ 인스턴스에 ssh로 접속하고 stress를 사용하여 Auto Scaling 작동 테스트 하기
![6](https://github.com/sub-blind/oz_front/assets/58137602/3ecf725b-d986-4b62-b57d-5427290f4ec9)
7. 모든 리소스 정리하기
![7](https://github.com/sub-blind/oz_front/assets/58137602/83f2aa23-6384-4b94-8879-32b1650675a3)
