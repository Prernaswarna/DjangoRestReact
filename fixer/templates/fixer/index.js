'use strict'

class MyComponent extends React.Component{
        constructor(props){
                super(props);
                this.state={
                        error=Null;
                        isLoaded=False;
                        code=[];
                };
        }

        componentDidMount(){
                fetch("https://internet.channeli.in/oauth/authorise/?client_id=k9IXT2RD811seHEj8858BIo24rVCCDHsY50ucEj9<&redirect_url=127.0.0.8000/user/4/confirm")
                .then(res=>res.json())
                .then(
                        (result)=>{
                                this.setState({
                                        isLoaded=True,
                                        code = result.code});
                                },
                        (error)=>{
                                this.setState({
                                        isLoaded=True,
                                        error
                                                });
                                }
                        )
                }
        render(){
                const {error , isLoaded , code } = this.state;
                if(error){
                        return <div>Error : {error.message} </div>
                }else if(!isLoaded){
                        return <div>Loading...</div>
                }else{
                        return(code);
                        }
                }
        }
}
ReactDOM.render(
        <MyComponenet/>
        document.getElementById('loginbutton');
);
