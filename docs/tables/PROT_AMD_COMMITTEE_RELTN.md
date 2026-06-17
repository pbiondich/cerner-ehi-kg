# PROT_AMD_COMMITTEE_RELTN

> This table contains the required committees for a particular amendment's activation.

**Description:** Protocol amendment and committee relationship table.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COMMITTEE_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the committee table. This field identifies the commitee that is related to the protocol amendment. |
| 3 | `EDIT_IND` | DOUBLE | NOT NULL |  | This field indicates whether the validate_ind field can be edited. |
| 4 | `PROT_AMD_COMMITTEE_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the Prot_amd_committee_reltn table. It is an internal system assigned number. |
| 5 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the prot_amendment table. This field identifies the protocol amendment that is related to the committee. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VALIDATE_IND` | DOUBLE | NOT NULL |  | The relationship between committee and amendment is selected as needing validated for when a protocol amendment is activated. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMITTEE_ID` | [COMMITTEE](COMMITTEE.md) | `COMMITTEE_ID` |
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |

