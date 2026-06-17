# OAUTH_BUSINESS_ASSOC

> Contains OAuth information for Millennium "Business Associations". For the purposes of this table, a "Business Association" is an individual, group, or organization contained within the domain that acts as an oAuth consumer of Cerner's Cloud Services. A Business Entity is identified by a URI, the content of which is specified by the solution that defined it.

**Description:** OAUTH BUSINESS ASSOCIATIONS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BUSINESS_ASSOC_NAME` | VARCHAR(2000) | NOT NULL |  | The URI that identifies the Business Association |
| 3 | `OAUTH_ACCESS_ENDPOINT` | VARCHAR(2000) |  |  | Specifies the URL endpoint for acquiring tokens for this business entity. If NULL, the domain default endpoint will be used. |
| 4 | `OAUTH_BUSINESS_ASSOC_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `OAUTH_CONSUMER_KEY_TXT` | VARCHAR(2000) | NOT NULL |  | The business association's oAuth consumer key. |
| 6 | `PRINCIPAL` | VARCHAR(50) |  |  | The name of the last principal to modify this row. |
| 7 | `ROOT_KEY_TXT` | VARCHAR(64) | NOT NULL |  | Alias for the root key used by the proxy service to generate the SECRETS. |
| 8 | `SECRETS` | LONGBLOB |  |  | Encrypted information maintained by the cloud proxy service. Also contains signatures validating the authenticity of the row. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

