# IO_TOTAL_DEFINITION

> Definition of how a I&O total should be calculated.

**Description:** I&O Total Definition  
**Table type:** REFERENCE  
**Primary key:** `IO_TOTAL_DEFINITION_ID`  
**Columns:** 16  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `IO_TOTAL_DEFINITION_ID` | DOUBLE | NOT NULL | PK | Identifies the primary key for this specific definition for an I&O |
| 4 | `IO_TOTAL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | FK FROM IO_TOTAL_GROUP_DEFINITION. This is the grouper for the definitions. |
| 5 | `PREV_IO_TOTAL_DEFINITION_ID` | DOUBLE | NOT NULL | FK→ | Identifies the original primary key for this row. |
| 6 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | Identifies the DTA this definition is associated with. |
| 7 | `TOTAL_DEFINITION_NAME` | VARCHAR(200) | NOT NULL |  | Name of the definition. |
| 8 | `TOTAL_DURATION` | DOUBLE | NOT NULL |  | Total duration in minutes |
| 9 | `TOTAL_DURATION_TYPE_CD` | DOUBLE | NOT NULL |  | Total duration type |
| 10 | `TOTAL_OPERATION_TYPE_CD` | DOUBLE | NOT NULL |  | Operation to use to calculate the total |
| 11 | `TOTAL_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of calculation to perform. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IO_TOTAL_GROUP_ID` | [IO_TOTAL_GROUP_DEFINITION](IO_TOTAL_GROUP_DEFINITION.md) | `IO_TOTAL_GROUP_ID` |
| `PREV_IO_TOTAL_DEFINITION_ID` | [IO_TOTAL_DEFINITION](IO_TOTAL_DEFINITION.md) | `IO_TOTAL_DEFINITION_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CE_IO_TOTAL_RESULT](CE_IO_TOTAL_RESULT.md) | `IO_TOTAL_DEFINITION_ID` |
| [IO_TOTAL_DEFINITION](IO_TOTAL_DEFINITION.md) | `PREV_IO_TOTAL_DEFINITION_ID` |

