# GROUP_TYPE_KEYS

> Contains: Group code value; script task numbers for ?selecting existing groups and getting list to chose from?

**Description:** OMF Group type keys.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DESCRIPTION` | VARCHAR(255) |  |  | Description of group type key |
| 2 | `GROUPING_CD` | DOUBLE | NOT NULL | FK→ | Group type code value. |
| 3 | `KEY_SELECT_LIST` | VARCHAR(255) |  |  | Task number for getting existing groupings (95300) when key_seq=1; and filter_meaning to get list of values if key_seq=2. |
| 4 | `KEY_SEQ` | DOUBLE | NOT NULL |  | Sequence for uniqueness. |
| 5 | `NUM_VALUE` | DOUBLE | NOT NULL |  | For key_seq = 1, the group's code value. Not used for key_seq = 2. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GROUPING_CD` | [GROUP_TYPE](GROUP_TYPE.md) | `GROUPING_CD` |

