Darf `switch` mit `std::string` kombiniert werden? -> Nein
<!--SR:!2024-08-01,13,290-->
Definiere einen `enum` Ampelfarben. Wo sind Kommas und wo Semikolons zu setzen? -> `enum class traffic_light { RED, YELLOW, GREEN };`
<!--SR:!2024-08-04,16,290-->
Wirf eine Fehlermeldung des Typs `invalid_argument` -> `throw std::invalid_arguemnt("ERROR MSG");`
<!--SR:!2024-08-02,14,294-->
Lies den Inhalt einer Fehlermeldung aus. -> `e.what();`

<!--SR:!2024-08-03,15,294-->
Fange einen Fehler ab und gib dessen Error Message auf `cerr` aus.
?
```cpp
try {
	<possibly failing code>
} catch(std::<expected error> &e) {
	std::cerr << e.what() << std::endl;
} catch (...) { // catch ANY error
	std::cerr << "unknown error" << std::endl;
}
```
<!--SR:!2024-07-22,4,281-->


<!--SR:!2024-07-20,4,279-->

<!--SR:!2024-07-19,4,274-->