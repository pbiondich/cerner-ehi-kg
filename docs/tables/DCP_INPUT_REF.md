# DCP_INPUT_REF

> contains the definition of a single input control on a form

**Description:** Description of the input control  
**Table type:** REFERENCE  
**Primary key:** `DCP_INPUT_REF_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DCP_INPUT_REF_ID` | DOUBLE | NOT NULL | PK | unique id of input control |
| 3 | `DCP_SECTION_INSTANCE_ID` | DOUBLE | NOT NULL |  | Identifies the section version that the input control is part of. |
| 4 | `DCP_SECTION_REF_ID` | DOUBLE | NOT NULL |  | Identifies the section that the input control is part of. |
| 5 | `DESCRIPTION` | VARCHAR(200) |  |  | textual description of input control |
| 6 | `INPUT_REF_SEQ` | DOUBLE |  |  | sequence number of input control to control order that it is placed on the section |
| 7 | `INPUT_TYPE` | DOUBLE |  |  | numeric indicator to identify what type of control the input is. |
| 8 | `MODULE` | VARCHAR(100) |  |  | Name of DLL module that implements control. If the name is blank then the control is implemented in pvFormControls.dll. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CNT_INPUT_KEY](CNT_INPUT_KEY.md) | `DCP_INPUT_REF_ID` |

