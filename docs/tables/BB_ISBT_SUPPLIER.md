# BB_ISBT_SUPPLIER

> Holds blood supplier organizations (including transfusion facilities that pool ISBT products) and their ISBT Facility Identification numbers.

**Description:** Blood Bank ISBT Supplier  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BB_ISBT_SUPPLIER_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a blood supplier by their ISBT Facility Identification number and the organization id. |
| 6 | `INVENTORY_AREA_CD` | DOUBLE | NOT NULL |  | For pooling facilities, the inventory areas that should use this license and registration number with the corresponding FIN from bb_isbt_supplier. 0 means all locations for this supplier (organization) use this FIN (and the same license and registration) |
| 7 | `ISBT_SUPPLIER_FIN` | VARCHAR(5) |  |  | Facility Identification Number for an ISBT supplier which is in the product number barcode. (Alphanumeric) |
| 8 | `LICENSE_NBR_TXT` | VARCHAR(15) |  |  | The license number of a facility for licensed products. |
| 9 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the organization for this supplier. |
| 10 | `REGISTRATION_NBR_TXT` | VARCHAR(15) |  |  | Contains the FDA Registration number for supplier facility. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

