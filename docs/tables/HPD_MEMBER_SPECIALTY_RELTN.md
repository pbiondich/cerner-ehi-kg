# HPD_MEMBER_SPECIALTY_RELTN

> Stores the Membership-Specialty relations between a Membership (HPD_MEMBERSHIP) and a Specialty (HPD_SPECIALTY)

**Description:** Healthcare Provider Directory Membership-Specialty Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `HPD_MEMBERSHIP_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key that corresponds to a single row on the HPD_MEMBERSHIP table |
| 3 | `HPD_MEMBER_SPECIALTY_RELTN_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `HPD_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key that corresponds to a single row on the HPD_SPECIALTY table |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HPD_MEMBERSHIP_ID` | [HPD_MEMBERSHIP](HPD_MEMBERSHIP.md) | `HPD_MEMBERSHIP_ID` |
| `HPD_SPECIALTY_ID` | [HPD_SPECIALTY](HPD_SPECIALTY.md) | `HPD_SPECIALTY_ID` |

