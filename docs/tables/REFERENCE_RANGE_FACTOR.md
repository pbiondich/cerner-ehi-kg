# REFERENCE_RANGE_FACTOR

> Stores reference range information for a specific discrete task assay. Used to store all reference range paramaters to flex numeric or alpha result types.

**Description:** Reference Range Factor  
**Table type:** REFERENCE  
**Primary key:** `REFERENCE_RANGE_FACTOR_ID`  
**Columns:** 57  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AGE_FROM_MINUTES` | DOUBLE |  |  | Defines the beginning age in minutes for a defined reference range. |
| 6 | `AGE_FROM_UNITS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific age units (such as days, months, years, and so on) for the beginning age reference range. |
| 7 | `AGE_TO_MINUTES` | DOUBLE |  |  | Defines the ending age in minutes for a defined reference range. |
| 8 | `AGE_TO_UNITS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific age units (such as days, months, years, and so on) for the ending age reference range. |
| 9 | `ALPHA_RESPONSE_IND` | DOUBLE |  |  | Indicates whether alpha responses apply for the reference range defined. (No longer used) |
| 10 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 11 | `CODE_SET` | DOUBLE |  |  | Defines the code set used to validate reference ranges for assays with the result type of "online code set". |
| 12 | `CRITICAL_HIGH` | DOUBLE |  |  | Defines the critical high reference range. |
| 13 | `CRITICAL_IND` | DOUBLE |  |  | Indicates whether critical result reference ranges are defined. |
| 14 | `CRITICAL_LOW` | DOUBLE |  |  | Indicates the critical low value for a reference range. |
| 15 | `DEFAULT_RESULT` | DOUBLE |  |  | Defines the default result value associated with specified reference range. |
| 16 | `DEF_RESULT_IND` | DOUBLE |  |  | Indicates whether the default result value has been defined for the reference range. |
| 17 | `DELTA_CHECK_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the type of delta checking algorithm to use. |
| 18 | `DELTA_CHK_FLAG` | DOUBLE |  |  | Defines the type of delta checking to perform. |
| 19 | `DELTA_MINUTES` | DOUBLE |  |  | Defines the specific number of minutes used to calculate the delta checking algorithm. |
| 20 | `DELTA_VALUE` | DOUBLE |  |  | Defines the value used to perform delta checking. |
| 21 | `DILUTE_IND` | DOUBLE |  |  | Indicates whether a dilution will be required for results that exceed the limits of the linear high range column. |
| 22 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the encounter type (i.e. patient type) used to flex the reference range. |
| 23 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 24 | `FEASIBLE_HIGH` | DOUBLE |  |  | Defines the feasible high value for the defined reference range. Typically, this is the limit above which no result is possible. |
| 25 | `FEASIBLE_IND` | DOUBLE |  |  | Indicates whether feasible limits exist for the reference range. |
| 26 | `FEASIBLE_LOW` | DOUBLE |  |  | Defines the feasible low value for the reference range. Typically, this is the limit below which no result is possible. |
| 27 | `GESTATIONAL_IND` | DOUBLE |  |  | Indicates whether the reference range defined is for the gestational age. |
| 28 | `LINEAR_HIGH` | DOUBLE |  |  | Defines the linear high limit for the reference range. Result values above this limit are considered out of the linear high limits of the service resource specified. |
| 29 | `LINEAR_IND` | DOUBLE |  |  | Indicates whether linear limits exist for the reference range. |
| 30 | `LINEAR_LOW` | DOUBLE |  |  | Defines the linear low limit for the reference range. Result values below this limit are considered out of the linear low limits of the service resource specified. |
| 31 | `MINS_BACK` | DOUBLE |  |  | Used to calculate the minutes back from the previous result to default the value for the current result for CareNet applications. |
| 32 | `NORMAL_HIGH` | DOUBLE |  |  | Defines the normal high reference range value for a specific discrete task assay. |
| 33 | `NORMAL_IND` | DOUBLE |  |  | Indicates whether normal ranges are built for the reference range specified. |
| 34 | `NORMAL_LOW` | DOUBLE |  |  | Defines the normal low value for the reference range. |
| 35 | `ORGANISM_CD` | DOUBLE | NOT NULL |  | (Currently not implemented) |
| 36 | `PATIENT_CONDITION_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the patient condition that is stored for the reference range. (Currently not implemented) |
| 37 | `PRECEDENCE_SEQUENCE` | DOUBLE |  |  | Used to determine which reference range row to use when all matching criteria are the same. |
| 38 | `REFERENCE_RANGE_FACTOR_ID` | DOUBLE | NOT NULL | PK | A unique, internal, system-assigned number that identifies a specific reference range factor row. |
| 39 | `REF_RANGE_RULE_IND` | DOUBLE | NOT NULL |  | Indicates that there are reference flexing rules. These are stored on the ref_range_factor_rule table. |
| 40 | `REVIEW_HIGH` | DOUBLE |  |  | Defines the review high reference range limit for a discrete task assay. |
| 41 | `REVIEW_IND` | DOUBLE |  |  | Indicates whether review range values are defined for the reference range. |
| 42 | `REVIEW_LOW` | DOUBLE |  |  | Defines the value for the review low reference range. |
| 43 | `SENSITIVE_HIGH` | DOUBLE |  |  | Defines the value for the sensitive high reference range. |
| 44 | `SENSITIVE_IND` | DOUBLE |  |  | Indicates whether sensitive range values are defined for the reference range. |
| 45 | `SENSITIVE_LOW` | DOUBLE |  |  | Defines the sensitive low value for the reference range. |
| 46 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the service resource (such as instrument, bench, or sub section) that will affect the reference range defined. A value of zero represents any service resource. |
| 47 | `SEX_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the sex adjustment for the reference range. A value of zero represents any sex. |
| 48 | `SPECIES_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the species for the defined reference range. A value of zero represents any species. |
| 49 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specimen type for the defined reference range. A value of zero represents any specimen type. |
| 50 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | A unique code value that identifies the discrete task assay to which the reference range applies. |
| 51 | `UNITS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific units of measure to be appended to results for the defined reference range. |
| 52 | `UNKNOWN_AGE_IND` | DOUBLE |  |  | Indicates whether the reference range stored is for unknown ages. |
| 53 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 54 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 55 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 56 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 57 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (8)

| From table | Column |
|------------|--------|
| [ADVANCED_DELTA](ADVANCED_DELTA.md) | `REFERENCE_RANGE_FACTOR_ID` |
| [ALPHA_RESPONSES](ALPHA_RESPONSES.md) | `REFERENCE_RANGE_FACTOR_ID` |
| [ALPHA_RESPONSES_CATEGORY](ALPHA_RESPONSES_CATEGORY.md) | `REFERENCE_RANGE_FACTOR_ID` |
| [CHARGE_EVENT_ACT](CHARGE_EVENT_ACT.md) | `REFERENCE_RANGE_FACTOR_ID` |
| [PERFORM_RESULT](PERFORM_RESULT.md) | `REFERENCE_RANGE_FACTOR_ID` |
| [PROP_RESULT](PROP_RESULT.md) | `REFERENCE_RANGE_FACTOR_ID` |
| [REF_RANGE_FACTOR_RULE](REF_RANGE_FACTOR_RULE.md) | `REFERENCE_RANGE_FACTOR_ID` |
| [REF_RANGE_NOTIFY_TRIG](REF_RANGE_NOTIFY_TRIG.md) | `REFERENCE_RANGE_FACTOR_ID` |

