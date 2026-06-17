# PCA_PCP_STATS

> Provides outcome measure statistics at the PCP/Group grain.

**Description:** Power Chart Analytics Primary Care Physician Statistics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MEAS_CONTRAINDCT_CNT` | DOUBLE | NOT NULL |  | Count of those measures that were contraindicated for this PCP/Outcome. |
| 2 | `MEAS_EXPCTN_MET_CNT` | DOUBLE | NOT NULL |  | Count of the outcomes that were met for this PCP/Measure/Outcome. |
| 3 | `MEAS_EXPCTN_NOT_MET_CNT` | DOUBLE | NOT NULL |  | Count of the outcomes that were not met for this PCP/Measure/Outcome. |
| 4 | `MEAS_MEDCR_CONTRAINDCT_CNT` | DOUBLE | NOT NULL |  | Count of those outcomes that were contraindicated for this PCP/Measure/Outcome for persons identified as Medicare Part B. |
| 5 | `MEAS_MEDCR_EXPCTN_MET_CNT` | DOUBLE | NOT NULL |  | Count of those outcomes that were met for this PCP/Measure/Outcome for persons identified as Medicare Part B. |
| 6 | `MEAS_MEDCR_EXPCTN_NOT_MET_CNT` | DOUBLE | NOT NULL |  | Count of those outcomes that were not met for this PCP/Measure/Outcome for persons identified as Medicare Part B. |
| 7 | `MEAS_MEDCR_OUTCOME_CNT` | DOUBLE | NOT NULL |  | Count of the total number of outcomes for this PCP/Measure/Outcome for persons identified as Medicare Part B. |
| 8 | `MEAS_NAME` | VARCHAR(60) | NOT NULL |  | Textual display value of the quality measure. |
| 9 | `MEAS_OUTCOME_CNT` | DOUBLE | NOT NULL |  | Count of the total number of outcomes for this PCP/Measure/Outcome. |
| 10 | `MEAS_OUTCOME_NAME` | VARCHAR(60) | NOT NULL |  | Textual display value for the outcome. |
| 11 | `MEAS_PCP_GROUP_ID` | DOUBLE | NOT NULL |  | The identifier for the Primary Care Physician group. |
| 12 | `MEAS_PCP_GROUP_NAME` | VARCHAR(60) | NOT NULL |  | The textual display value for the name of the Primary Care Physician group. |
| 13 | `MEAS_PCP_ID` | DOUBLE | NOT NULL |  | The identifier for the Primary Care Physician. |
| 14 | `MEAS_PCP_NAME` | VARCHAR(60) | NOT NULL |  | Textual display value for the primary care provider. |
| 15 | `MEAS_PCP_NPI_TXT` | VARCHAR(200) | NOT NULL |  | NPI of the primary care provider. |
| 16 | `MEAS_PCP_ORG_NAME` | VARCHAR(100) | NOT NULL |  | Organization of the primary care provider. |
| 17 | `MEAS_PCP_TAXID_TXT` | VARCHAR(200) | NOT NULL |  | Tax ID of the primary care provider. |
| 18 | `PCA_PCP_STATS_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the PCA_PCP_STATS table. |
| 19 | `TOPIC_NAME` | VARCHAR(60) | NOT NULL |  | Textual display value of the quality topic. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

