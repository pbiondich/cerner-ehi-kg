# BR_ELIG_PROV_MEAS_RELTN

> Stores the quality measures associated to a chosen eligible provider.

**Description:** Bedrock Eligible Provider Measure Relation  
**Table type:** REFERENCE  
**Primary key:** `BR_ELIG_PROV_MEAS_RELTN_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | The provider that is being measured. |
| 4 | `BR_ELIG_PROV_MEAS_RELTN_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the BR_ELIG_PROV_MEAS_RELTN table. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `MEASURE_SEQ` | DOUBLE | NOT NULL |  | The order in which the quality measures are evaluated when checking for meaningful use measures. |
| 7 | `ORIG_BR_ELIG_PROV_MEAS_R_ID` | DOUBLE | NOT NULL | FK→ | Used for versioning. Contains the value of the PK for a particular set of rows in BR_ELIG_PROV_MEAS_RELTN. |
| 8 | `PCA_QUALITY_MEASURE_ID` | DOUBLE | NOT NULL | FK→ | The Quality Measure being tracked for this provider. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_ELIGIBLE_PROVIDER_ID` | [BR_ELIGIBLE_PROVIDER](BR_ELIGIBLE_PROVIDER.md) | `BR_ELIGIBLE_PROVIDER_ID` |
| `ORIG_BR_ELIG_PROV_MEAS_R_ID` | [BR_ELIG_PROV_MEAS_RELTN](BR_ELIG_PROV_MEAS_RELTN.md) | `BR_ELIG_PROV_MEAS_RELTN_ID` |
| `PCA_QUALITY_MEASURE_ID` | [PCA_QUALITY_MEASURE](PCA_QUALITY_MEASURE.md) | `PCA_QUALITY_MEASURE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_ELIG_PROV_MEAS_RELTN](BR_ELIG_PROV_MEAS_RELTN.md) | `ORIG_BR_ELIG_PROV_MEAS_R_ID` |

