# CNT_INPUT_KEY

> INPUT KEY

**Description:** CNT INPUT KEY  
**Table type:** REFERENCE  
**Primary key:** `CNT_INPUT_KEY_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CNT_INPUT_KEY_ID` | DOUBLE | NOT NULL | PK | Sequence generated ID - PRIMARY KEY |
| 2 | `CNT_INPUT_PVC_NAME` | VARCHAR(32) | NOT NULL |  | The name portion of the name/value pair that is stored on a row in this table. |
| 3 | `CNT_SECTION_KEY2_ID` | DOUBLE | NOT NULL | FK→ | Sequence generated ID (Value: 0.0) - FROM CNT_SECTION_KEY2 |
| 4 | `DCP_INPUT_REF_ID` | DOUBLE | NOT NULL | FK→ | Unique ID of Input Control (FK value from DCP_INPUT_REF) |
| 5 | `INPUT_DESCRIPTION` | VARCHAR(200) | NOT NULL |  | Textual description of input control |
| 6 | `INPUT_REF_SEQ` | DOUBLE | NOT NULL |  | Sequence number of input control to control order that it is placed on the section. |
| 7 | `INPUT_TYPE` | DOUBLE |  |  | Numeric indicator to identify what type of control the input is. |
| 8 | `MODULE_NAME` | VARCHAR(100) | NOT NULL |  | Name of DLL module that implements control. If the name is blank then the control is implemented in pvFormControls.dll |
| 9 | `SECTION_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Section |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNT_SECTION_KEY2_ID` | [CNT_SECTION_KEY2](CNT_SECTION_KEY2.md) | `CNT_SECTION_KEY2_ID` |
| `DCP_INPUT_REF_ID` | [DCP_INPUT_REF](DCP_INPUT_REF.md) | `DCP_INPUT_REF_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CNT_GRID](CNT_GRID.md) | `CNT_INPUT_KEY_ID` |
| [CNT_INPUT](CNT_INPUT.md) | `CNT_INPUT_KEY_ID` |

