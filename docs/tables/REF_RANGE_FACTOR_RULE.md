# REF_RANGE_FACTOR_RULE

> Contains rules related to the reference range factor table.

**Description:** Reference Range Factor Rule  
**Table type:** REFERENCE  
**Primary key:** `REF_RANGE_FACTOR_RULE_ID`  
**Columns:** 35  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CRITICAL_HIGH` | DOUBLE | NOT NULL |  | Defines the critical high limit for the reference range. Result values above this limit are considered out of the normal limits of the service resource specified. |
| 6 | `CRITICAL_LIMIT_IND` | DOUBLE | NOT NULL |  | Indicates whether critical limits exist for the reference range rule. |
| 7 | `CRITICAL_LOW` | DOUBLE | NOT NULL |  | Defines the Critical Low limit for the reference range. Result values below this limit are considered out of the critical low limits of the service resource specified. |
| 8 | `DEFAULT_RESULT_IND` | DOUBLE | NOT NULL |  | Indicates whether the default result value has been defined for the reference range. |
| 9 | `DEFAULT_RESULT_VALUE` | DOUBLE | NOT NULL |  | Defines the default result value associated with specified reference range. |
| 10 | `FEASIBLE_HIGH` | DOUBLE | NOT NULL |  | Defines the feasible high limit for the reference range. Result values above this limit are considered out of the feasible limits of the service resource specified. |
| 11 | `FEASIBLE_LIMIT_IND` | DOUBLE | NOT NULL |  | Indicates whether feasible limits exist for the reference range rule. |
| 12 | `FEASIBLE_LOW` | DOUBLE | NOT NULL |  | defines the feasible low limit for the reference range. Result values below this limit are considered out of the feasible low limits of the service resource specified. |
| 13 | `FROM_GESTATION_DAYS` | DOUBLE | NOT NULL |  | Contains the from side of the range of the gestational age of the patient at the birth measured in days. |
| 14 | `FROM_HEIGHT` | DOUBLE | NOT NULL |  | The from side of the range of height through which the reference is flexed. |
| 15 | `FROM_HEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | Contains the unit of measure for the height. |
| 16 | `FROM_WEIGHT` | DOUBLE | NOT NULL |  | The from side of the range of weight through which the reference is flexed. |
| 17 | `FROM_WEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | Contains the unit of measure for the weight. |
| 18 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Contains the location of the patient when the results are documented. |
| 19 | `MINUTES_BACK` | DOUBLE |  |  | Used to calculate the minutes back from the previous result to default the value for the current result for CareNet applications. |
| 20 | `NORMAL_HIGH` | DOUBLE | NOT NULL |  | Defines the normal high limit for the reference range. Result values above this limit are considered out of the normal high limits of the service resource specified. |
| 21 | `NORMAL_LIMIT_IND` | DOUBLE | NOT NULL |  | Indicates whether the normal limits exist for the reference range rule. |
| 22 | `NORMAL_LOW` | DOUBLE | NOT NULL |  | Defines the normal low limit for the reference range. Result values below this limit are considered out of the normal low limits of the service resource specified. |
| 23 | `REFERENCE_RANGE_FACTOR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the reference range factor related to this rule. |
| 24 | `REF_RANGE_FACTOR_RULE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a rule for a given reference range factor. |
| 25 | `RESULT_MEASUREMENT_UNIT_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific units of measure to be appended to results for the defined reference range. |
| 26 | `TO_GESTATION_DAYS` | DOUBLE | NOT NULL |  | Contains the to side of the range of the gestational age of the patient at birth measured in days. |
| 27 | `TO_HEIGHT` | DOUBLE | NOT NULL |  | Contains the to side of the range of the height through which the reference is flexed. |
| 28 | `TO_HEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | Contains the unit of measure for the height. |
| 29 | `TO_WEIGHT` | DOUBLE | NOT NULL |  | Contains the to side of the range of weight through which the reference is flexed. |
| 30 | `TO_WEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | Contains the unit of measure for the weight. |
| 31 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 32 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 33 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 34 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 35 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REFERENCE_RANGE_FACTOR_ID` | [REFERENCE_RANGE_FACTOR](REFERENCE_RANGE_FACTOR.md) | `REFERENCE_RANGE_FACTOR_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ALPHA_RESPONSE_RULE](ALPHA_RESPONSE_RULE.md) | `REF_RANGE_FACTOR_RULE_ID` |

