# PAT_ED_DOC_ACTIVITY

> This tables hold the patient education document Instructions activity.

**Description:** PAT ED DOC ACTIVITY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DOC_LANG_ID_VALUE` | DOUBLE | NOT NULL |  | The language id value that corresponds to the activity instruction. |
| 3 | `DOC_TYPES` | VARCHAR(255) |  |  | Document types to which this instruction activity belongs. |
| 4 | `INSTRUCTION_DT_TM` | DATETIME |  |  | The date and time when this instruction was printed. |
| 5 | `INSTRUCTION_NAME` | VARCHAR(1000) | NOT NULL |  | The instruction name that is displayed to the user |
| 6 | `INSTRUCTION_USER_ID` | DOUBLE | NOT NULL | FK→ | The user id of who printed this instruction |
| 7 | `KEY_DOC_IDENT` | VARCHAR(255) |  |  | A unique key that identifies this instruction. |
| 8 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This column hold the long text id form the long text table where the insruction given to the patient is stored. |
| 9 | `PAT_ED_DOC_ACTIVITY_ID` | DOUBLE | NOT NULL |  | Primary key to this table. It uniquely stores each instruction given to the patient. |
| 10 | `PAT_ED_DOC_ID` | DOUBLE | NOT NULL | FK→ | Unique key for each doucment created for a patients encounter.Column |
| 11 | `PAT_ED_DOMAIN_CD` | DOUBLE | NOT NULL |  | The content domain that the activity instruction was selected from |
| 12 | `PAT_ED_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Reference to original patient education instructionColumn |
| 13 | `PRINT_IND` | DOUBLE | NOT NULL |  | 1 if printed and 0 if not. |
| 14 | `REFR_TEXT_ID` | DOUBLE | NOT NULL |  | Reference to original patient education instructions text if from the ref_text table |
| 15 | `STATUS_CD` | DOUBLE | NOT NULL |  | Status of the Instruction (from code set 8) |
| 16 | `TYPE_FLAG` | DOUBLE |  |  | Determines the type of instruction that was saved to the activity. Null = undertermined, 0 = Patient Education instruction not suggested, 1 = Infobutton instruction, 2 = Patient Education instruction suggested |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INSTRUCTION_USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LONG_TEXT_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `PAT_ED_DOC_ID` | [PAT_ED_DOCUMENT](PAT_ED_DOCUMENT.md) | `PAT_ED_DOCUMENT_ID` |
| `PAT_ED_RELTN_ID` | [PAT_ED_RELTN](PAT_ED_RELTN.md) | `PAT_ED_RELTN_ID` |

