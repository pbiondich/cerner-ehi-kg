# LH_QRDA_PROV_DET

> This table is used to store elements that are used to provide additional information for each provider needed in QRDA Category 1 and 3 file for submission. This table is at the grain of one provider per row.

**Description:** LH_QRDA_PROV_DET  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 52

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AUTHOR_CITY` | VARCHAR(50) |  |  | The author's location city |
| 3 | `AUTHOR_NPI` | VARCHAR(50) |  |  | The author's national provider ID |
| 4 | `AUTHOR_ORG_NAME` | VARCHAR(50) |  |  | The name of the author's organization |
| 5 | `AUTHOR_STATE` | VARCHAR(50) |  |  | The author's location state |
| 6 | `AUTHOR_STREET_ADDR` | VARCHAR(200) |  |  | The author's street address |
| 7 | `AUTHOR_STREET_ADDR2` | VARCHAR(200) |  |  | The second line of the author's street address |
| 8 | `AUTHOR_TELECOM` | VARCHAR(50) |  |  | The author's phone number |
| 9 | `AUTHOR_ZIPCODE` | VARCHAR(50) |  |  | The author's location zip code |
| 10 | `BR_CPC_ID` | DOUBLE | NOT NULL |  | The id of the cpc practice site set in bedrock |
| 11 | `BR_GPRO_ID` | DOUBLE | NOT NULL |  | The id of the provider group set in bedrock |
| 12 | `BR_GPRO_SUB_ID` | DOUBLE |  |  | Unique generated number that identifies a single row on the BR_GPRO_SUB table. |
| 13 | `CMS_PROGRAM` | VARCHAR(100) |  |  | Type of submission program: 'NQF', 'PQRS', 'GPRO-PQRS', 'GPRO-NQF', 'CPC' |
| 14 | `CUSTODIAN_CITY` | VARCHAR(50) |  |  | The custodian's location city |
| 15 | `CUSTODIAN_NPI` | VARCHAR(50) |  |  | The custodian's national provider ID |
| 16 | `CUSTODIAN_ORG_NAME` | VARCHAR(50) |  |  | The name of the custodian's organization |
| 17 | `CUSTODIAN_STATE` | VARCHAR(50) |  |  | The custodian's location state |
| 18 | `CUSTODIAN_STREET_ADDR` | VARCHAR(200) |  |  | The custodian's street address |
| 19 | `CUSTODIAN_STREET_ADDR2` | VARCHAR(200) |  |  | The second line of the custodian's street address |
| 20 | `CUSTODIAN_TELECOM` | VARCHAR(50) |  |  | The custodian's phone number |
| 21 | `CUSTODIAN_ZIPCODE` | VARCHAR(50) |  |  | The custodian's location zip code |
| 22 | `D_PRSNL_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the Other Template section is related (i.e. lh_qrda_pqrs_id) |
| 23 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 24 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 25 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 26 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 27 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 28 | `LEGAL_AUTH_CITY` | VARCHAR(50) |  |  | The legal authenticator's location city |
| 29 | `LEGAL_AUTH_NPI` | VARCHAR(50) |  |  | The legal authenticator's national provider ID |
| 30 | `LEGAL_AUTH_ORG_NAME` | VARCHAR(50) |  |  | The name of the legal authenticator's organization |
| 31 | `LEGAL_AUTH_STATE` | VARCHAR(50) |  |  | The legal authenticator's location state |
| 32 | `LEGAL_AUTH_STREET_ADDR` | VARCHAR(200) |  |  | The legal authenticator's street address |
| 33 | `LEGAL_AUTH_STREET_ADDR2` | VARCHAR(200) |  |  | The second line of the legal authenticator's street address |
| 34 | `LEGAL_AUTH_TELECOM` | VARCHAR(50) |  |  | The legal authenticator's phone number |
| 35 | `LEGAL_AUTH_ZIPCODE` | VARCHAR(50) |  |  | The legal authenticator's location zip code |
| 36 | `LH_QRDA_PROV_DET_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_QRDA_PROV_DET table. |
| 37 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 38 | `PROV_CITY` | VARCHAR(100) |  |  | The provider's location city |
| 39 | `PROV_ORG_NAME` | VARCHAR(255) |  |  | The name of the provider's organization |
| 40 | `PROV_STATE` | VARCHAR(50) |  |  | The provider's location state |
| 41 | `PROV_STREET_ADDR` | VARCHAR(200) |  |  | The provider's street address |
| 42 | `PROV_STREET_ADDR2` | VARCHAR(200) |  |  | The second line of the provider's street address |
| 43 | `PROV_TELECOM` | VARCHAR(50) |  |  | The provider's phone number |
| 44 | `PROV_ZIPCODE` | VARCHAR(50) |  |  | The provider's location zip code |
| 45 | `REPORTING_CATEGORY` | DOUBLE |  |  | Indicates if the report category is QRDA 1 or QRDA 3. |
| 46 | `REPORTING_YEAR` | DOUBLE |  |  | Stores the reporting year. |
| 47 | `SRC_UPDT_DT_TM` | DATETIME |  |  | Indicates the actual time when the row was inserted or updated at the source. This column is used only for date extraction and will not be populated on the client site. |
| 48 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | This column is updated with the name of the source program that loaded these rows into this table in Quality Clearinghouse when the Power Insight extracts were executed. This column is used only for date extraction and will not be populated on the client site. |
| 49 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 51 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 52 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

