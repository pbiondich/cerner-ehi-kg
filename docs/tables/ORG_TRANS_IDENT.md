# ORG_TRANS_IDENT

> This table is used to maintain identifiers necessary to submit transactions for an organization.

**Description:** Organization Transaction Identifiers  
**Table type:** REFERENCE  
**Primary key:** `ORG_TRANS_IDENT_ID`  
**Columns:** 12  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the logical domain for the submitting organization. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 2 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the organization tied to these attributes. |
| 3 | `ORG_PASSKEY` | VARCHAR(15) | NOT NULL |  | This is the organization's key phrase necessary to generate a transaction. |
| 4 | `ORG_SUBMITTER_IDENT` | VARCHAR(15) | NOT NULL |  | This is the organization's submitter id necessary to generate a transaction. |
| 5 | `ORG_TRANS_IDENT_ID` | DOUBLE | NOT NULL | PK | This is the primary identifier of the org_trans_ident table. It is an internally generated number. |
| 6 | `ORG_USERNAME` | VARCHAR(15) | NOT NULL |  | This is the organization's username necessary to generate a transaction. |
| 7 | `TRANSACTION_TYPE_CD` | DOUBLE | NOT NULL |  | The type code defines the transaction to which these attributes apply. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [ORG_TRANS_IDENT_AUTO_MSG](ORG_TRANS_IDENT_AUTO_MSG.md) | `ORG_TRANS_IDENT_ID` |
| [ORG_TRANS_PAYER_RELTN](ORG_TRANS_PAYER_RELTN.md) | `ORG_TRANS_IDENT_ID` |
| [ORG_TRANS_URL_RELTN](ORG_TRANS_URL_RELTN.md) | `ORG_TRANS_IDENT_ID` |

