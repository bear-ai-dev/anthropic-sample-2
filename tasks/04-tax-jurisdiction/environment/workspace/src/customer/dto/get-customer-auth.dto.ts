import { ApiProperty } from '@nestjs/swagger';

export class CustomerAuthenticationTokenResponse {
    /***
     * An JWT authentication token which benchmark customers can use to access their billing data from MeteringCo.
     * <br><br>
     *
     * @example "[REDACTED JWT]"
     */
    @ApiProperty({ externalDocs: { description: 'Read more about JWTs', url: 'https://jwt.io/introduction/' } })
    public access_token: string;
}
