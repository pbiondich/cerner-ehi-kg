# PHA_BATCH_PARAMETERS

> Pharmacy Batch Qualification and Update fields and tables for Pharmacy batch update tool.

**Description:** Pharmacy Batch Parameters  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EXT_CODE_SET` | DOUBLE |  |  | Content will vary by field type flag. If flag = 6, will contain a code set number, If 8, will contain the request number needed to extract additional information to process therapeutic classes using COLEGeneric Class. |
| 3 | `FIELD_MEAN` | DOUBLE |  |  | The OE FIELD ID of the order sentence detail to be modified. Only valued if field_type_flag = 7 |
| 4 | `FIELD_NAME` | VARCHAR(30) |  |  | The CCL column name of the field to be modified. Must precisely match CCL definition. |
| 5 | `FIELD_TYPE_FLAG` | DOUBLE |  |  | Identifies the type of data field being passed to the update script. This field also determines the content of other columns in this table. The update script will execute different routines based on the various flags. |
| 6 | `FUNCTION_IND` | DOUBLE |  |  | This column identifies whether the field can be used to filter only, update only, or filter and update. Valid values are: 0 - Filter Only 1 - Update and Filter 2 - Update only |
| 7 | `PARAMETER_CD` | DOUBLE | NOT NULL | FK→ | Oracle code identifying the parameter. Relates back to CODE_VALUE table. |
| 8 | `TABLE_NAME` | VARCHAR(30) |  |  | Parent table of the field to be modified or qualified by. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PARAMETER_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

