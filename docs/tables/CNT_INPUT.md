# CNT_INPUT

> INPUT

**Description:** CNT INPUT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CNT_INPUT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY - Sequence generated ID |
| 2 | `CNT_INPUT_KEY_ID` | DOUBLE | NOT NULL | FK→ | Sequence generated ID FROM CNT_INPUT_KEY table - (Value: 0.0) |
| 3 | `CNT_SECTION_KEY2_ID` | DOUBLE | NOT NULL | FK→ | Sequence generated ID from CNT_SECTION_KEY2 table - (Value: 0.0) |
| 4 | `CODE_VALUE_DISP` | VARCHAR(40) |  |  | Used to look up merge_id not written to a table |
| 5 | `COND_SECT_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Conditional Section DTA |
| 6 | `DCP_INPUT_REF_ID` | DOUBLE | NOT NULL |  | unique id of input control from table DCP_INPUT_REF |
| 7 | `DTA_ACT_DISP` | VARCHAR(40) |  |  | Used to look up merge_id not written to a table |
| 8 | `EVENT_CD` | DOUBLE | NOT NULL |  | Event code for DTAs |
| 9 | `EVENT_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier FK to CNT_CODE_VALUE_KEY |
| 10 | `INPUT_DESCRIPTION` | VARCHAR(200) | NOT NULL |  | textual description of input control |
| 11 | `INPUT_REF_SEQ` | DOUBLE | NOT NULL |  | sequence number of input control to control order that it is placed on the section |
| 12 | `INPUT_SEQUENCE` | DOUBLE |  |  | Sequence of name value pair |
| 13 | `MERGE_ID` | DOUBLE | NOT NULL |  | The MERGE_ID value from table NAME_VALUE_PREFS. This is a PE-NAME/PE-ID relationship so no specific root entity name or sequence name can be specified. MERGE_NAME specifies the table name. |
| 14 | `MERGE_NAME` | VARCHAR(100) | NOT NULL |  | name of the table referenced by merge_id |
| 15 | `MERGE_UID` | VARCHAR(100) | NOT NULL |  | The universal unique identifier for the referenced row. |
| 16 | `NAME_VALUE_PREFS_ID` | DOUBLE | NOT NULL |  | The primary id of the table this row references |
| 17 | `PVC_NAME` | VARCHAR(32) | NOT NULL |  | The name portion of the name/value pair that is stored on a row in this table. |
| 18 | `PVC_VALUE` | VARCHAR(255) |  |  | The value portion of the name/value pair that is stored on a row in this table. |
| 19 | `SECTION_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Section |
| 20 | `TASK_ASSAY_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for DTA |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNT_INPUT_KEY_ID` | [CNT_INPUT_KEY](CNT_INPUT_KEY.md) | `CNT_INPUT_KEY_ID` |
| `CNT_SECTION_KEY2_ID` | [CNT_SECTION_KEY2](CNT_SECTION_KEY2.md) | `CNT_SECTION_KEY2_ID` |

