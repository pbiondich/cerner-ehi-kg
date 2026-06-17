# SI_SYSTEM_ORG_RELTN

> This table will store relationships between Contributor Systems, Organizations, and Alias Pools.

**Description:** System Integration System Organization Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | This Alias Pool needs to have an OID valued on the SI_OID table to qualify to be selected. |
| 2 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 3 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the Organization ID that is part of the relationship between contributor systems and alias pools. This value is required. |
| 4 | `PRIMARY_IND` | DOUBLE | NOT NULL |  | This is the primary relationship for the system, organization, and alias pool when this indicator is set. |
| 5 | `SI_SYSTEM_ORG_RELTN_ID` | DOUBLE | NOT NULL |  | Unique Identifier for the SI_SYSTEM_ORG_RELTN table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

