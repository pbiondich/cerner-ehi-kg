# REF_CD_MAP_HEADER

> Header table used to store associations betwen results (events, orders, etc.) and reference codes (nomenclature_ids).

**Description:** Reference Code Mapping Header  
**Table type:** ACTIVITY  
**Primary key:** `REF_CD_MAP_HEADER_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter financial id for the result. |
| 2 | `EVENT_ID` | DOUBLE | NOT NULL |  | The clinical_event for the result associated with a reference code. |
| 3 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person the result pertains to. |
| 4 | `REF_CD_MAP_HEADER_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the REF_CD_MAP_HEADER table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [REF_CD_MAP_DETAIL](REF_CD_MAP_DETAIL.md) | `REF_CD_MAP_HEADER_ID` |

