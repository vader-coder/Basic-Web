import javax.servlet.*;

/*
http://www.eg.bucknell.edu/~mead/Java-tutorial/servlets/client-interaction/http-methods.html
can we have doGet and doPost be the same?
*/

public class BasicServerlet extends HttpServlet {
    public void doGet (HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {
        Map<String, Object> requestMap = request.getParameterMap();
        //seperate module to handle request. later may try to get it to JSON instead of String.
        String myResponse = ResponseHandler.response(requestMap);
        response.setContentType("application/json");//json 
        PrintWriter writer = response.getWriter();
        writer.println(myResponse);
        writer.close();
    }
}