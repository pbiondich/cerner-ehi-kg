# PEER_REVIEWER

> Contains information aboutt review, done on a protocol by anothether institution

**Description:** PEER REVIEWER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the organization table. This field identifies the institution performing the peer review. For this purpose, an institution can be another hospital, research institute, drug company, government agency, etc. |
| 2 | `PEER_REVIEWER_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the peer_reviewer table. It is an internal system assigned number. |
| 3 | `PEER_REVIEWER_STATUS_CD` | DOUBLE | NOT NULL |  | This field contains the code that defines the status of the peer review. |
| 4 | `PROT_MASTER_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the prot_master table. This field identifies the protocol that is subject to peer review. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PROT_MASTER_ID` | [PROT_MASTER](PROT_MASTER.md) | `PROT_MASTER_ID` |

