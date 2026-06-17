# ORG_TRANS_PAYER_RELTN

> This table is used to maintain relations between facility organizations and payer organizations. A relation must exist for transactions to be allowed between organizations.

**Description:** Organization Transaction Payer Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALT_PAYER_ORG_ID` | DOUBLE | NOT NULL | FK→ | This is the primary identifier of the organization table. the relation defines which alternate payers may have transactions submitted to them from the given facility. |
| 2 | `ORG_TRANS_IDENT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the facility transactions associated to the payer. It is a foreign key to the ORG_TRANS_IDENT table. |
| 3 | `ORG_TRANS_PAYER_RELTN_ID` | DOUBLE | NOT NULL |  | The unique primary key for this table. It is an internally generated number. |
| 4 | `PAYER_ORG_ID` | DOUBLE | NOT NULL | FK→ | This is the primary identifier of the organization table. The relation defines which payers may have transactions submitted to them from the given facility. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALT_PAYER_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ORG_TRANS_IDENT_ID` | [ORG_TRANS_IDENT](ORG_TRANS_IDENT.md) | `ORG_TRANS_IDENT_ID` |
| `PAYER_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

