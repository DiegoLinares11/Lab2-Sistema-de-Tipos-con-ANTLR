from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor
from custom_types import IntType, FloatType, StringType, BoolType

class TypeCheckVisitor(SimpleLangVisitor):

  def visitMulDiv(self, ctx: SimpleLangParser.MulDivContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for * or /: {} and {}".format(left_type, right_type))

  def visitAddSub(self, ctx: SimpleLangParser.AddSubContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for + or -: {} and {}".format(left_type, right_type))
  
  def visitInt(self, ctx: SimpleLangParser.IntContext):
    return IntType()

  def visitFloat(self, ctx: SimpleLangParser.FloatContext):
    return FloatType()

  def visitString(self, ctx: SimpleLangParser.StringContext):
    return StringType()

  def visitBool(self, ctx: SimpleLangParser.BoolContext):
    return BoolType()

  def visitParens(self, ctx: SimpleLangParser.ParensContext):
    return self.visit(ctx.expr())
  
  def visitModulo(self, ctx: SimpleLangParser.ModuloContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))

    if not isinstance(left_type, IntType) or not isinstance(right_type, IntType):
        raise TypeError("Modulo (%) only supports integer operands")
    return IntType()

  def visitPower(self, ctx: SimpleLangParser.PowerContext):
      left_type = self.visit(ctx.expr(0))
      right_type = self.visit(ctx.expr(1))

      if isinstance(left_type, StringType) or isinstance(right_type, StringType) \
        or isinstance(left_type, BoolType) or isinstance(right_type, BoolType):
          raise TypeError("Exponentiation (^) does not support string or bool operands")
      return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

  def visitMulDiv(self, ctx: SimpleLangParser.MulDivContext):
      left_type = self.visit(ctx.expr(0))
      right_type = self.visit(ctx.expr(1))

      if ctx.op.text == '/' and isinstance(right_type, IntType) and ctx.expr(1).getText() == '0':
          raise TypeError("Division by zero is not allowed")

      if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
          return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
      else:
          raise TypeError("Unsupported operand types for * or /: {} and {}".format(left_type, right_type))

