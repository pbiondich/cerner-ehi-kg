# OPS2_JOB_TEMPLATE

> The operations job template table stores information about the available templates for creating a job and its default parameter values.

**Description:** Operations Job Template  
**Table type:** REFERENCE  
**Primary key:** `OPS2_JOB_TEMPLATE_ID`  
**Columns:** 12  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `EXTERNAL_USERNAME` | VARCHAR(100) |  |  | The name of the non-Millennium (e.g. Olympus) user that modified the record. |
| 5 | `OPS2_JOB_TEMPLATE_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the OPS2_JOB_TEMPLATE table. |
| 6 | `ORIG_OPS2_JOB_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | This field is used to track versions of the job templates. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 7 | `TEMPLATE_NAME` | VARCHAR(40) | NOT NULL |  | The name of the template to create a job. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORIG_OPS2_JOB_TEMPLATE_ID` | [OPS2_JOB_TEMPLATE](OPS2_JOB_TEMPLATE.md) | `OPS2_JOB_TEMPLATE_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [OPS2_JOB](OPS2_JOB.md) | `OPS2_JOB_TEMPLATE_ID` |
| [OPS2_JOB_TEMPLATE](OPS2_JOB_TEMPLATE.md) | `ORIG_OPS2_JOB_TEMPLATE_ID` |
| [OPS2_STEP_TEMPLATE](OPS2_STEP_TEMPLATE.md) | `OPS2_JOB_TEMPLATE_ID` |

