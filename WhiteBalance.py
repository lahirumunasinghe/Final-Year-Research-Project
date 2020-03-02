function get_avg_a_b ()
    sum_a=0
    sum_b=0

    -- first find average color in CIE Lab space
    for y=0, height-1 do
      for x=0, width-1 do
        l,a,b = get_lab(x,y)
        sum_a, sum_b = sum_a+a, sum_b+b
      end
      progress(y/height)
    end

    avg_a=sum_a/(width*height)
    avg_b=sum_b/(width*height)

    return avg_a,avg_b
    end

function shift_a_b(a_shift, b_shift)
    for y=0, height do
      for x=0, width do
        l,a,b = get_lab(x,y)

        -- scale the chroma distance shifted according to amount of
        -- luminance. The 1.1 overshoot is because we cannot be sure
        -- to have gotten the data in the first place.
        a_delta = a_shift * (l/100) * 1.1
        b_delta = b_shift * (l/100) * 1.1
        a,b = a+a_delta, b+b_delta

        set_lab(x,y,l,a,b)
      end
      progress(y/height)
    end
    flush()
end

function grayworld_assumption()
  avg_a, avg_b = get_avg_a_b()
  shift_a_b(-avg_a, -avg_b)
end

grayworld_assumption()
