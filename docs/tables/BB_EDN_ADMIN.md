# BB_EDN_ADMIN

> This table contains the administration information from an Electronic Delivery Note message structure

**Description:** Blood Bank Electronic Delivery Note Administration  
**Table type:** ACTIVITY  
**Primary key:** `BB_EDN_ADMIN_ID`  
**Columns:** 16  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMIN_DT_TM` | DATETIME | NOT NULL |  | The data and time the electronic data note was dispatched or acknowledged. |
| 2 | `BB_EDN_ADMIN_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies administration information from an electronic delivery note message structure. |
| 3 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 4 | `DESTINATION_INV_AREA_CD` | DOUBLE | NOT NULL |  | Inventory Area where the product will be received. |
| 5 | `DESTINATION_LOC_CD` | DOUBLE | NOT NULL |  | Refers to the location the products in the Electronic Delivery Note to which the file will be shipped. |
| 6 | `DISPATCH_NBR_TXT` | VARCHAR(12) | NOT NULL |  | Contains the dispatch number from the electronic delivery note file. |
| 7 | `EDN_COMPLETE_IND` | DOUBLE | NOT NULL |  | Indicates if the electronic delivery note has been completed. |
| 8 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Contains the unique identifier for the long blob text corresponding to the electronic delivery note file. |
| 9 | `ORDER_NBR_IDENT` | VARCHAR(12) | NOT NULL |  | Uniquely identifies the order number from the electronic delivery note file. |
| 10 | `PROTOCOL_NBR` | DOUBLE | NOT NULL |  | Identifies the protocol (1 - 5) of the electronic delivery note file.0 if Electronic receipt (i.e. Donor Inbound) |
| 11 | `SOURCE_ORG_ID` | DOUBLE | NOT NULL | FK→ | Contains the unique identifier of the organization from which the electronic delivery note was sent. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `SOURCE_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [BB_EDN_DSCRPNCY_OVRD](BB_EDN_DSCRPNCY_OVRD.md) | `BB_EDN_ADMIN_ID` |
| [BB_EDN_PRODUCT](BB_EDN_PRODUCT.md) | `BB_EDN_ADMIN_ID` |

