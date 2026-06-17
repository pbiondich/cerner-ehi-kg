# BR_SCH_TEMP_RES_R

> Stores the resources from the a data collection spreadsheet associated with a default schedule template (on the BR_SCH_TEMPLATE table).

**Description:** BR_SCH_TEMP_RES_R  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLY_BEGIN_DT_TM` | DATETIME |  |  | The internal date representation of the apply_begin_str if it contains a date in the expected format. |
| 2 | `APPLY_BEGIN_STR` | VARCHAR(40) |  |  | A string containing the day that this resource should start having the template applied to its' schedule. Format mm/dd/yyyy |
| 3 | `APPLY_END_DT_TM` | DATETIME |  |  | The internal date representation of the apply_begin_str if it contains a date in the expected format. |
| 4 | `APPLY_END_STR` | VARCHAR(40) |  |  | A string containing the day that this resource should stop having the template applied to its' schedule. Format mm/dd/yyyy |
| 5 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 6 | `BR_SCH_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The id of the template that this resource row is associated with. |
| 7 | `BR_SCH_TEMP_RES_R_ID` | DOUBLE | NOT NULL |  | Primary index and unique identifier for rows on this table. |
| 8 | `RESOURCE_CD` | DOUBLE | NOT NULL |  | If the resource_name matched up with a valid sch_resource during the import, the code value of the resource will be here. |
| 9 | `RESOURCE_NAME` | VARCHAR(100) | NOT NULL |  | The name of the resource as entered into the data collection worksheet. |
| 10 | `RESOURCE_STATUS_FLAG` | DOUBLE | NOT NULL |  | Future use, values not defined (as of 3/3/06) |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_SCH_TEMPLATE_ID` | [BR_SCH_TEMPLATE](BR_SCH_TEMPLATE.md) | `BR_SCH_TEMPLATE_ID` |

