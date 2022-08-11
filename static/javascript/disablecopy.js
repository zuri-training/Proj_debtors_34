//jsQuery inserted into the head of the html '''''' <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.0/jquery.min.js"></script> '''''''

<script>
      $(document).ready(function() {
          $('body').bind('cut copy', function(e) {
              e.preventDefault();
            })
        });
    </script>