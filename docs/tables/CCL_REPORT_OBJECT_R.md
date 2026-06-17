# CCL_REPORT_OBJECT_R

> CCL Report Object relationship

**Description:** CCL Report Object relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `OBJECT_ID` | DOUBLE | NOT NULL | FK→ | Reference to object defined on CCL_REPORT_OBJECT |
| 2 | `REP_OBJ_RELTN_ID` | DOUBLE | NOT NULL |  | Report object relation identifier |
| 3 | `SECTION_ID` | DOUBLE | NOT NULL | FK→ | Reference to Layout section defined in CCL_LAYOUT_SECTION |
| 4 | `SECTION_SEQUENCE` | DOUBLE | NOT NULL |  | The sequence of the section_id in relation to the Object_id which uses the section |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OBJECT_ID` | [CCL_REPORT_OBJECT](CCL_REPORT_OBJECT.md) | `OBJECT_ID` |
| `SECTION_ID` | [CCL_LAYOUT_SECTION](CCL_LAYOUT_SECTION.md) | `SECTION_ID` |

