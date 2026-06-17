# PRSNL_GROUP_POOL

> Stores information specific to the 'pool' use of a prsnl group. Pools are a group of providers, typically working together and sharing Inbox Tasks.

**Description:** Personnel Group Pool  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 3 | `OUTSIDE_ADD_IND` | DOUBLE | NOT NULL |  | Can Add Prsnl To Pool From Outside Org. Indicates if prsnl who are not members of the pool's organization can add new pool members. |
| 4 | `OUTSIDE_FORWARD_IND` | DOUBLE | NOT NULL |  | Can Forward To Pool From Outside Org. Indicates if prsnl who are not members of the pool's organization can forward Inbox items to the pool. |
| 5 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Personnel Group Identification. The source Personnel Group which Uniquely identifies the Pool. |
| 6 | `PRSNL_GROUP_POOL_ID` | DOUBLE | NOT NULL |  | The Primary Key for this table. |
| 7 | `SCH_FLEX_ID` | DOUBLE | NOT NULL | FK→ | The flex-id used for the flex-engine. Comes from SCH_FLEX_STRING |
| 8 | `SELF_ASSIGN_LEADER_IND` | DOUBLE | NOT NULL |  | Allow user to self-declare team leader |
| 9 | `SELF_ENROLL_IND` | DOUBLE | NOT NULL |  | Allow users to opt-in or opt-out of membership |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `SCH_FLEX_ID` | [SCH_FLEX_STRING](SCH_FLEX_STRING.md) | `SCH_FLEX_ID` |

