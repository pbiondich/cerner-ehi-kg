# HPD_ORGANIZATION

> Stores the networked organization information

**Description:** Healthcare Provider Directory Organization  
**Table type:** REFERENCE  
**Primary key:** `HPD_ORGANIZATION_ID`  
**Columns:** 16  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BILLING_ADDRESS` | VARCHAR(255) |  |  | Billing Address of the Organization |
| 3 | `FAX_NUMBER_TXT` | VARCHAR(25) |  |  | Fax Number of the Organization |
| 4 | `HPD_ORGANIZATION_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 5 | `LABELED_URI` | VARCHAR(255) |  |  | Uniform Resource Identifier for the organization. As an example this can be the organization's web site URL. |
| 6 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 7 | `MAILING_ADDRESS` | VARCHAR(255) |  |  | Mailing Address of the Organization |
| 8 | `ORGANIZATION_NAME` | VARCHAR(255) | NOT NULL |  | Name of the Organization |
| 9 | `PARENT_HPD_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key that corresponds to a single row on the HPD_ORGANIZATION table to represent the parent organization. |
| 10 | `REVISION_NBR` | DOUBLE | NOT NULL |  | Current revision of the table. This should be incremented 1 higher than the highest revision on the table. All rows in the same update should have the same revision. |
| 11 | `TELEPHONE_NUMBER_TXT` | VARCHAR(25) |  |  | Telephone Number of the Organization |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PARENT_HPD_ORGANIZATION_ID` | [HPD_ORGANIZATION](HPD_ORGANIZATION.md) | `HPD_ORGANIZATION_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [HPD_ADDRESS](HPD_ADDRESS.md) | `HPD_ORGANIZATION_ID` |
| [HPD_MEMBERSHIP](HPD_MEMBERSHIP.md) | `HPD_ORGANIZATION_ID` |
| [HPD_ORGANIZATION](HPD_ORGANIZATION.md) | `PARENT_HPD_ORGANIZATION_ID` |

