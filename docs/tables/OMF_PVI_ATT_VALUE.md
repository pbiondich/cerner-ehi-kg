# OMF_PVI_ATT_VALUE

> Holds lower level attribute values for PowerVision components and viewer styles.

**Description:** OMF PVI ATT VALUE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTRIB_ID` | DOUBLE |  |  | Id of parent attribute. |
| 2 | `COMPONENT_ID` | DOUBLE |  |  | Id of parent PowerVision component. |
| 3 | `OMF_PV_ITEM_ID` | DOUBLE |  |  | Id of the parent PowerVision saved view or template. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VAL1` | VARCHAR(255) |  |  | Generic string to hold values. |
| 10 | `VAL2` | VARCHAR(255) |  |  | Generic string to hold values. |
| 11 | `VAL3` | VARCHAR(255) |  |  | Generic string to hold values. |
| 12 | `VAL4` | VARCHAR(255) |  |  | Generic string to hold values. |
| 13 | `VAL5` | VARCHAR(255) |  |  | Generic string to hold values. |
| 14 | `VALUE_ID` | DOUBLE | NOT NULL |  | Unique id for this table. |
| 15 | `VALUE_TYPE` | VARCHAR(255) |  |  | Description of the type of value that is being stored. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

