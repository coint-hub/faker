import itertools

from .. import Provider as LoremProvider

# 알수 없는 소스
# https://www.loremipzum.com/vi/
_source = """Nhưng tôi phải giải thích cho bạn hiểu làm thế nào mà tất cả ý tưởng sai lầm về việc tố cáo niềm vui và ca ngợi nỗi đau đã ra đời và tôi sẽ cung cấp cho bạn một bản tường trình đầy đủ về hệ thống, cũng như giải thích những lời dạy thực tế của nhà thám hiểm chân lý vĩ đại, Người xây dựng nên hạnh phúc của con người. Không ai từ chối, không thích hay tránh xa thú vui, vì nó là thú vui, mà vì những ai không biết theo đuổi thú vui một cách hợp lý sẽ gặp phải những hậu quả vô cùng đau đớn. Cũng không có ai yêu hoặc theo đuổi hoặc mong muốn tự mình đạt được nỗi đau, bởi vì đó là nỗi đau, nhưng đôi khi xảy ra những trường hợp mà sự vất vả và đau đớn có thể mang lại cho anh ta một số niềm vui lớn. Nhưng ai có quyền nhận lỗi với một người đàn ông chọn cách tận hưởng một niềm vui mà không gây ra hậu quả khó chịu, hoặc một người trốn tránh một nỗi đau không tạo ra khoái cảm? Mặt khác, chúng tôi tố cáo với sự phẫn nộ chính đáng và chán ghét những người đàn ông bị cám dỗ và mất tinh thần bởi sự quyến rũ của thú vui nhất thời, bị dục vọng làm cho mù quáng, đến nỗi họ không thể lường trước được nỗi đau và rắc rối sắp xảy ra; và trách nhiệm bình đẳng thuộc về những người thất bại trong nhiệm vụ của họ do yếu kém về ý chí, điều này cũng giống như nói khi thu mình lại vì vất vả và đau đớn. Những trường hợp này là hoàn toàn đơn giản và dễ dàng để phân biệt. Trong một giờ rảnh rỗi, khi quyền lực lựa chọn của chúng ta là không có khuôn mẫu và khi không có gì ngăn cản chúng ta có thể làm những gì chúng ta thích nhất, mọi niềm vui đều được chào đón và mọi nỗi đau đều tránh được. Nhưng trong một số trường hợp nhất định và do các yêu cầu về nghĩa vụ hoặc nghĩa vụ kinh doanh, sẽ thường xuyên xảy ra những thú vui phải từ chối và chấp nhận những khó chịu. Do đó, nhà thông thái luôn tuân giữ nguyên tắc lựa chọn này trong những vấn đề: anh ta từ chối những thú vui để đảm bảo những thú vui khác lớn hơn, hoặc anh ta chịu đựng nỗi đau để tránh những cơn đau tồi tệ hơn."""


class Provider(LoremProvider):
    """Implement lorem provider for ``vi_VN`` locale."""

    word_connector = " "
    sentence_punctuation = "."
    word_list = tuple(
        set(
            filter(
                bool,
                map(
                    lambda x: x.replace('.', '').strip().removesuffix('!').removesuffix('?').removesuffix(','),
                    itertools.chain.from_iterable(map(lambda x: x.split(' '), _source.splitlines()))
                )
            )
        )
    )
