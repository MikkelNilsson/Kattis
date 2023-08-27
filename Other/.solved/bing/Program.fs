
type Trie = T of int * Map<char, Trie>

let Empty = T (0, Map.empty)


let rec insert inp (T (c,m)) =
    match inp with
    | [] -> 
        printf "%d\n" (c)
        T (c + 1, m)
    | x :: xs -> 
        T (c + 1,
            match Map.tryFind x m with
            | None -> Map.add x (insert xs Empty) m
            | Some y -> Map.add x (insert xs y) m
            )

let rec run (t:Trie) n' =
    match n' with
    | 0 -> 0
    | n -> 
        let inp = System.Console.ReadLine ()
        run (insert [for c in inp -> c] t) (n-1)



[<EntryPoint>]
let main argv = 
    let n = int <| System.Console.ReadLine ()
    let tree = T (0, Map.empty)
    run tree n
    