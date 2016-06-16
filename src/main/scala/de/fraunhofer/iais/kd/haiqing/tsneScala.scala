package de.fraunhofer.iais.kd.haiqing

/**
 * Created by hwang on 15.06.16.
 */

import java.io.{PrintWriter, File}

import com.jujutsu.tsne._
import com.jujutsu.utils._


object tsneScala {
  def main(args: Array[String]): Unit = {
    //val tsne = new Tsne

    val initial_dims = 55
    val perplexity = 20.0
    val X = MatrixUtils.simpleRead2DMatrix(new File(args(0)))



    //println(MatrixOps.doubleArrayToPrintString(X, ", ", 50,10))
    val tsne = new FastTSne()
    val Y = tsne.tsne(X, 2, initial_dims, perplexity)
    //println(MatrixOps.doubleArrayToPrintString(Y, ", ", 50,10))
    val outFile = new PrintWriter(new File(args(1)))
    for (i <- 0 until Y.size) {
      for (j <- 0 until Y(0).size)
        outFile.write(Y(i)(j) + " ")
      outFile.write("\n")
    }
    outFile.close()
  }
}
