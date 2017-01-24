package wekatest;

import java.io.File ;
import java.util.ArrayList;
import java.util.Random;

import weka.classifiers.lazy.IBk;
import weka.classifiers.Evaluation;
import weka.core.converters.ConverterUtils.DataSource;
import weka.core.Instances;
import weka.core.UnsupportedAttributeTypeException;

public class Ibk {

    public static void main(String[] args) throws Exception {
        Integer[] percentages = new Integer[]{10};
        for (Integer percentage : percentages) {
            File dir = new File(String.format("../new/osn-data/tweets_selected/features_step3/aggregated/weka/%d", percentage));
            for (File file : dir.listFiles()) {
                DataSource source = new DataSource(file.getAbsolutePath());
                Instances data = source.getDataSet();
                data.setClassIndex(data.numAttributes() - 1);
                IBk ibk = new IBk();
                try {
                    ibk.buildClassifier(data);
                } catch(UnsupportedAttributeTypeException ignored) {
                    continue;
                }
                Evaluation evaluation = new Evaluation(data);
                try {
                    evaluation.crossValidateModel(ibk, data, 10, new Random(1));
                } catch(IllegalArgumentException ignored) {
                    continue;
                }
                System.out.println(file.getName());
                System.out.println(evaluation.toSummaryString());
            }
        }
    }
}