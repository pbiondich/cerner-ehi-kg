# ASSAY_RESOURCE_LOT

> Creates a relationship between the assays for a resource that will be used for a given control lot.

**Description:** Assay Resource Lot  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABS_HIGH` | DOUBLE |  |  | Defines the high value for comparing a result value against to see if the result should be flagged as high. |
| 2 | `ABS_LOW` | DOUBLE |  |  | Defines the low value for comparing a result value against to see if the result should be flagged as low. |
| 3 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ARL_ID` | DOUBLE | NOT NULL |  | A unique internal system assigned number that identifies a specific relationship between a service resource, discrete task assay, and a control lot. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CLINICAL_STD_DEV` | DOUBLE |  |  | Defines the standard deviation for a clinically significant value. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `LOT_ID` | DOUBLE | NOT NULL | FK→ | A unique internal system assigned number that identifies a specific control lot. Creates a relationship to the control lot table. |
| 9 | `MANF_HIGH` | DOUBLE |  |  | Defines the manufacturer defined high level for the discrete task assay and the control. |
| 10 | `MANF_LOW` | DOUBLE |  |  | Defines the manufacturer defined low level for the discrete task assay and control. |
| 11 | `MANF_MEAN` | DOUBLE |  |  | Defines the manufacturer defined mean for the discrete task assay and control. |
| 12 | `MANF_STD_DEV` | DOUBLE |  |  | Defines the manufacturer defined standard deviation for the discrete task assay and control. |
| 13 | `MEAN` | DOUBLE |  |  | Defines the expected mean for results to be compared against for the control lot. |
| 14 | `RULE_ID` | DOUBLE | NOT NULL |  | A unique internal system assigned number that identifies a specific quality control rule to be applied for the discrete task assay. |
| 15 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | A unique code value that identifies the specific service resource (i.e. instrument, bench) associated with the discrete task assay and control lot. |
| 16 | `STATISTICAL_STD_DEV` | DOUBLE |  |  | Defines the standard deviation for the discrete task assay. Used to determine the high and low value. |
| 17 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | A unique code value that identifies the specific discrete task assay associated with the control lot. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_ID` | [CONTROL_LOT](CONTROL_LOT.md) | `LOT_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

