package wekatest;

import java.io.File ;
import java.util.Random;

import weka.classifiers.Evaluation;
import weka.classifiers.bayes.NaiveBayes;
import weka.classifiers.trees.RandomForest;
import weka.core.converters.ConverterUtils.DataSource;
import weka.core.Instances;
 
public class WekaTest {
 
    public static void main(String[] args) throws Exception {
        File dir = 
        new File("/Users/chaima/dev/hourly/src/new/osn-data/tweets_selected/features_step3/aggregated/weka");
//        new File("/Users/chaima/dev/hourly/src/new/osn-data/tweets_selected__negative_are_features/features_step3/aggregated/weka");
        for (File file : dir.listFiles()) {
          if (file.getName().equals("all.csv")) {
            continue;
          }
          System.out.println(file.getName());
          DataSource source = new DataSource(file.getAbsolutePath());
          Instances data = source.getDataSet();
          data.setClassIndex(data.numAttributes() - 1);
          RandomForest rf = new RandomForest();
          Evaluation evaluation = new Evaluation(data);
          try {
            evaluation.crossValidateModel(rf, data, 10, new Random(1));
          } catch(IllegalArgumentException ignored) {
            continue;
          }
          System.out.println(evaluation.toSummaryString("\nResults\n======\n", true));
          //System.out.println(evaluation.rootMeanSquaredError());
      }
    }
}
