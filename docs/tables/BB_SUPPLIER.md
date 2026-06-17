# BB_SUPPLIER

> This table is only necessary for suppliers that use supplier prefixes and alpha translations on their product numbers.

**Description:** Defines the suppliers of blood for the hospital.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALPHA_TRANSLATION_IND` | DOUBLE |  |  | Determines whether the first two digits of the product number should be translated to a different character(s) for this supplier. Commonly used on Red Cross blood. |
| 6 | `BARCODE_VALUE` | CHAR(20) |  |  | The actual barcode value that is the FDA originating supplier prefix for this supplier. |
| 7 | `BB_SUPPLIER_ID` | DOUBLE | NOT NULL |  | The primary key to this table. An internal system-assigned number that ensures the uniqueness of every row on this table. |
| 8 | `DEFAULT_PREFIX_IND` | DOUBLE |  |  | Determines whether the supplier's prefix (ex. "09") should be displayed as a default at the time products are logged into the system from this supplier. |
| 9 | `ISBT_BARCODE` | VARCHAR(15) |  |  | Obsolete. This column is no longer being used. ISBT FIN of supplier. Used to scan supplier from the DIN field. |
| 10 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Links the row on this table to the actual organization defined for the blood bank supplier. |
| 11 | `PREFIX_IND` | DOUBLE |  |  | Determines whether this blood supplier ever ships blood products with an FDA originating supplier prefix on them. |
| 12 | `PREFIX_VALUE` | CHAR(5) |  |  | Defines the value of the FDA originating supplier prefix for this blood supplier, e.g., "09", which will be displayed as the leftmost digits of the product number. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

