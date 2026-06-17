# HPD_ADDRESS

> Stores the networked address information

**Description:** Healthcare Provider Directory Address  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADDRESS_TYPE_CD` | DOUBLE | NOT NULL |  | The code set value corresponding to the type of address (e.g. mailing, billing, business, etc.) |
| 3 | `CITY_NAME` | VARCHAR(100) |  |  | The text name of the city. |
| 4 | `HPD_ADDRESS_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `HPD_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key Value from the HPD_ORGANIZATION table. |
| 6 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the logical domain of the address. |
| 7 | `REVISION_NBR` | DOUBLE | NOT NULL |  | Highest revision on the table. All rows in the same update should have the same revision number. |
| 8 | `STATE_NAME` | VARCHAR(100) |  |  | The text name of the state or province. |
| 9 | `STREET_ADDRESS1` | VARCHAR(100) |  |  | The first line of the street address. |
| 10 | `STREET_ADDRESS2` | VARCHAR(100) |  |  | The second line of the street address. |
| 11 | `STREET_ADDRESS3` | VARCHAR(100) |  |  | The third line of the street address. Typically only used for international addresses. |
| 12 | `STREET_ADDRESS4` | VARCHAR(100) |  |  | The fourth line of the street address. Typically only used for international addresses. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `ZIPCODE_TXT` | VARCHAR(25) |  |  | The postal code for the address. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HPD_ORGANIZATION_ID` | [HPD_ORGANIZATION](HPD_ORGANIZATION.md) | `HPD_ORGANIZATION_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

