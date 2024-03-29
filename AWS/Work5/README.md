1. 로드밸런싱이 필요한 이유와 역할 설명해보기
   ![1](https://github.com/sub-blind/oz_front/assets/58137602/328411d1-1dfa-4e64-aa01-9534992b53ee)

   - 로드 밸런싱은 애플리케이션 서버와 방문자 또는 클라이언트 간의 인터넷 트래픽을 지시하고 제어합니다. 결과적으로 애플리케이션의 가용성, 확장성, 보안 및 성능이 향상됩니다.
   - 로드 밸런서는 워크로드를 가상 서버와 같은 다수의 컴퓨팅 리소스로 분산합니다. 로드 밸런서를 사용하면 애플리케이션의 가용성과 내결함성이 높아집니다.
   - 애플리케이션에 대한 요청의 전체적인 흐름을 방해하지 않고 필요에 따라 로드 밸런서에서 컴퓨팅 리소스를 추가 및 제거할 수 있습니다.
   - 로드 밸런서가 정상적인 대상에만 요청을 보내도록 컴퓨팅 리소스의 상태를 모니터링하는 상태 확인을 구성할 수 있습니다. 또한 컴퓨팅 리소스가 주요 작업에 집중할 수 있도록 암호화 및 복호화 작업을 로드 밸런서로 오프로드할 수 있습니다.

2. EC2 인스턴스 생성하기(서울 리전, Bitnami WordPress, t2.micro)
   ![2](https://github.com/sub-blind/oz_front/assets/58137602/f15bb10c-f51b-4f67-87ee-e0d09fa6e253)

3. ALB 생성하기 (EC2 인스턴스와 같은 리전) -대상 그룹도 함게 생성하고 EC2 인스턴스를 대상 그룹에 포함시키기
   ![3](https://github.com/sub-blind/oz_front/assets/58137602/526a9023-f205-4b8c-9fd5-04b7844fc3bd)

4. ALB의 주소를 통해 EC2 인스턴스에 접속하기
   ![4](https://github.com/sub-blind/oz_front/assets/58137602/116b995d-46bd-41e3-a196-7904ae967429)
5. ALB 생성하기 (EC2 인스턴스와 같은 리전) -대상 그룹도 함게 생성하고 EC2 인스턴스를 대상 그룹에 포함시키기
   ![3](https://github.com/sub-blind/oz_front/assets/58137602/526a9023-f205-4b8c-9fd5-04b7844fc3bd)

6. ALB의 주소를 통해 EC2 인스턴스에 접속하기
   ![4](https://github.com/sub-blind/oz_front/assets/58137602/116b995d-46bd-41e3-a196-7904ae967429)

7. EC2 인스턴스 종료하기
   ![5](https://github.com/sub-blind/oz_front/assets/58137602/70869368-a480-4bcc-a2f2-37c1ab4e8a39)
