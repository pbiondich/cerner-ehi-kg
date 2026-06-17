# NOTE_TYPE_LIST

> note type list

**Description:** List personal and role based list of note types  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_TYPE_CLASS_CD` | DOUBLE | NOT NULL |  | Identifies the encounter type class code to which this list is associated. If 0, then the list belongs to either an individual identified by prsnlid or role identified by the role_type_cd. |
| 2 | `NOTE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to note_type table |
| 3 | `NOTE_TYPE_LIST_ID` | DOUBLE | NOT NULL |  | unique primary key to note_type_list table |
| 4 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to prsnl table. Identifies the person whose list this item belongs to. if 0 then this item belongs to a role based list |
| 5 | `ROLE_TYPE_CD` | DOUBLE | NOT NULL |  | identifies the role to which this list is associated if 0 then the list belongs to an individual identified by prsnl_id |
| 6 | `SEQ_NUM` | DOUBLE |  |  | orders elements of a given list |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOTE_TYPE_ID` | [NOTE_TYPE](NOTE_TYPE.md) | `NOTE_TYPE_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

