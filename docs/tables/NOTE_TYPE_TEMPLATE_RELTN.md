# NOTE_TYPE_TEMPLATE_RELTN

> note_type_template_reltn

**Description:** This table relates a note type with a clinical note template.  
**Table type:** REFERENCE  
**Primary key:** `NOTE_TYPE_TEMPLATE_RELTN_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFAULT_IND` | DOUBLE |  |  | if value of 1 the template is the default template for the associated script. |
| 2 | `NOTE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to note_type table |
| 3 | `NOTE_TYPE_TEMPLATE_RELTN_ID` | DOUBLE | NOT NULL | PK | unique primary key to table. |
| 4 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to clinical_note_template. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOTE_TYPE_ID` | [NOTE_TYPE](NOTE_TYPE.md) | `NOTE_TYPE_ID` |
| `TEMPLATE_ID` | [CLINICAL_NOTE_TEMPLATE](CLINICAL_NOTE_TEMPLATE.md) | `TEMPLATE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PRSNL_LOC_TEMPLATE_RELTN](PRSNL_LOC_TEMPLATE_RELTN.md) | `NOTE_TYPE_TEMPLATE_RELTN_ID` |

