/* clase car */
class car{
  constructor(x,y,width,height){
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
  }
  draw(ctx){
    ctx.beginPath(); /* wtf */
    ctx.rect( /* wtf */
      this.x - this.width/2, 
      this.y - this.height/2,
      this.width,
      this.height
    ); /* es como decir, la x esta en el medio del coche por lo que si el witdth y la x empiezan en el mismo lugar, la x se divide por 2 del witdh para quedar a la mitad (en verdad no entiendo) */
    ctx.fill(); /* wtf */
  }
}