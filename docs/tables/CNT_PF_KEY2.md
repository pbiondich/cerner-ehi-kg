# CNT_PF_KEY2

> PF KEY

**Description:** CNT PF KEY  
**Table type:** REFERENCE  
**Primary key:** `CNT_PF_KEY_ID`  
**Columns:** 12  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CNT_PF_KEY_ID` | DOUBLE | NOT NULL | PK | Sequence generated ID - PRIMARY KEY |
| 2 | `DCP_FORMS_REF_ID` | DOUBLE | NOT NULL |  | Every form has a single entry in this table that describes the form such as name and definition - DCP_FORMS_REF |
| 3 | `FORM_DEFINITION` | VARCHAR(200) |  |  | Textual definition of the form. |
| 4 | `FORM_DESCRIPTION` | VARCHAR(200) |  |  | Textual description of the form |
| 5 | `FORM_INTERNAL_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for domain generated Powerform |
| 6 | `FORM_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Powerform |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VERSION_DT_TM` | DATETIME |  |  | Date the Powerform we extracted from source. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CNT_PF_SECTION_R](CNT_PF_SECTION_R.md) | `CNT_PF_KEY_ID` |
| [CNT_POWERFORM](CNT_POWERFORM.md) | `CNT_PF_KEY_ID` |

